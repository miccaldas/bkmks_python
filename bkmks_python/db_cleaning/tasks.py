"""
Deletes links, in the bookmakrs database, that answer 404.
"""
import isort
import requests
import snoop
from mysql.connector import Error, connect
from snoop import pp
from celery import Celery
from celery.schedules import crontab


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])

BROKER_URL = "redis://localhost:6379/0"
BACKEND_URL = "redis://localhost:6379/1"
app = Celery(
    "tasks",
    broker=BROKER_URL,
    backend=BACKEND_URL,
)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        check_urls.s(),
    )


@app.task(name="urls_check")
@snoop
def check_urls():
    """
    We iterate through the db links content, to see if they
    respond 404 or not. As some sites will negate automated
    traffic, we'll create an exception for 'ConnectionError'
    so as not stop the script execution.
    With a list of links that answered 404, we delete their
    entries from the database.
    """

    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="bkmks")
        cur = conn.cursor()
        query = """ SELECT * FROM bkmks"""
        cur.execute(query)
        records = cur.fetchall()
        conn.close()
    except Error as e:
        print("Error while connecting to db", e)

    urls_delete = []
    for url in records:
        try:
            req = requests.get(url[3])
        except requests.exceptions.ConnectionError:
            req.status_code = "Connection Refused"
        if req.status_code == 404:
            entry = url[0]
            urls_delete.append(entry)

    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="bkmks")
        cur = conn.cursor()
        for entry in urls_delete:
            query = f"DELETE FROM bkmks WHERE id = {entry}"
            cur.execute(query)
            conn.commit()
        conn.close()
    except Error as e:
        print("Error while connecting to db", e)


if __name__ == "__main__":
    check_urls()
