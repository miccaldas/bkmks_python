""" Module to insert bookmarks to database """

import click
import fire
from mysql.connector import Error, connect


def add():
    titulo = input(click.style(" Title? » ", fg="red", bold=True))
    comentario = input(click.style(" Comment » ", fg="red", bold=True))
    link = input(click.style(" Link » ", fg="red", bold=True))
    kwd1 = input(click.style(" Choose a keyword » ", fg="red", bold=True))
    kwd2 = input(click.style(" Choose another ... » ", fg="red", bold=True))
    kwd3 = input(click.style(" And another... » ", fg="red", bold=True))

    answers = [titulo, comentario, link, kwd1, kwd2, kwd3]

    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="bkmks")
        cur = conn.cursor()
        query = """ INSERT INTO bkmks (title, comment, link, k1, k2, k3) VALUES (%s, %s, %s, %s, %s, %s) """
        cur.execute(query, answers)
        conn.commit()

    except Error as e:
        print("Error while connecting to db", e)
    finally:
        conn.close()


if __name__ == "__main__":
    fire.Fire(add)
