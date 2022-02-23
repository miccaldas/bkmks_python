""" Module to see all of the database """

import click
import fire
from mysql.connector import Error, connect


def see():
    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="bkmks")
        cur = conn.cursor()
        query = """ SELECT * FROM bkmks"""
        cur.execute(query)
        records = cur.fetchall()
        for row in records:
            print(click.style(" [*] ID » ", fg="blue", bold=True), click.style(str(row[0]), fg="blue", bold=True))
            print(click.style(" [*] TITLE » ", fg="cyan", bold=True), click.style(str(row[1]), fg="cyan", bold=True))
            print(click.style(" [*] COMMENT » ", fg="blue", bold=True), click.style(str(row[2]), fg="blue", bold=True))
            print(click.style(" [*] LINK ? ", fg="cyan", bold=True), click.style(str(row[3]), fg="yellow", bold=True))
            print(click.style(" [*] KEYWORD 1 » ", fg="blue", bold=True), click.style(str(row[4]), fg="blue", bold=True))
            print(click.style(" [*] KEYWORD 2 » ", fg="cyan", bold=True), click.style(str(row[5]), fg="cyan", bold=True))
            print(click.style(" [*] KEYWORD 3 » ", fg="blue", bold=True), click.style(str(row[6]), fg="blue", bold=True))
            print(click.style(" [*] TIME » ", fg="cyan", bold=True), click.style(str(row[7]), fg="cyan", bold=True))
            print("\n")
            conn.close()
    except Error as e:
        print("Error while connecting to db", e)


if __name__ == "__main__":
    fire.Fire(see)
