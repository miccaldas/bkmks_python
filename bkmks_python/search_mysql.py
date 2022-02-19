""" Module to search the database """

import click
import fire
from mysql.connector import Error, connect
from rich import print
from rich.panel import Panel


def search():
    try:
        busca = input(click.style(" What are you searching for? ", fg="red", bold=True))
        conn = connect(host="localhost", user="mic", password="xxxx", database="bkmks")
        cur = conn.cursor()
        query = " SELECT id, title, comment, link, k1, k2, k3 FROM bkmks WHERE MATCH(title, comment, link, k1, k2, k3) AGAINST('" + busca + "') "
        cur.execute(query)
        records = cur.fetchall()
        for row in records:
            id = str(row[0])  # noqa: F841
            tit = row[1]  # noqa: F841
            comment = row[2]  # noqa: F841
            link = row[3]  # noqa: F841
            k1 = row[4]  # noqa: F841
            k2 = row[5]  # noqa: F841
            k3 = row[6]  # noqa: F841

            print(
                Panel(
                    f"[#bc4151]{tit}[/#bc4151]\n[#e6c0af]{comment}[/#e6c0af]\n[#a68e6a]#{k1}, #{k2}, #{k3}[/#a68e6a]\n[#d5ac82]{link}[/#d5ac82]",
                    title=f"{id}",
                    style="#6b6356",
                    highlight=True,
                )
            )
            print("\n")
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    fire.Fire(search)
