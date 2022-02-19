""" Module to delete bookmarks from the database """
from mysql.connector import connect, Error
import click


def delete():
    ident = input(click.style(' ID to delete? » ', fg='red', bold=True))

    try:
        conn = connect(
                        host="localhost",
                        user="mic",
                        password="xxxx",
                        database="bkmks")
        cur = conn.cursor()
        query = " DELETE FROM bkmks WHERE id = " + ident
        cur.execute(query)
        conn.commit()

    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if(conn):
            conn.close()


if __name__ == '__main__':
    delete()
