""" Module to insert bookmarks to database """

import click
import yake
from mysql.connector import Error, connect


def add():
    titulo = input(click.style(" Title? » ", fg="red", bold=True))
    comentario = input(click.style(" Comment » ", fg="red", bold=True))
    link = input(click.style(" Link » ", fg="red", bold=True))

    kw_extractor = yake.KeywordExtractor()  # noqa: F841
    text = comentario
    language = "en"
    max_ngram_size = 1
    deduplication_threshold = 0.9
    numOfKeywords = 10
    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
    keywords = custom_kw_extractor.extract_keywords(text)
    kwds = []
    for kw in keywords:
        kwds.append(kw[0])
    for idx, kwd in enumerate(kwds):
        print(click.style(f" {idx, kwd}", fg="red", bold=True))
    kwdcho = input(click.style("If you want to keep any of three keywords, type their number. ", fg="red", bold=True))
    if kwdcho != "":
        kwdchoi = kwdcho.split(" ")
        kwd_choice = [int(i) for i in kwdchoi]
        choices = []
        for i in kwd_choice:
            choice = [(idx, val) for (idx, val) in enumerate(kwds) if idx == i]
            choices.append(choice)
        flatter_choices = [i for sublist in choices for i in sublist]
        kwd_names = [f[1] for f in flatter_choices]
        if len(kwd_names) == 1:
            k1 = kwd_names[0]
            k2 = input(click.style(" Choose a keyword » ", fg="red", bold=True))
            k3 = input(click.style(" Choose another... » ", fg="red", bold=True))
        if len(kwd_names) == 2:
            k1 = kwd_names[0]
            k2 = kwd_names[1]
            k3 = input(click.style(" Choose a keyword » ", fg="red", bold=True))
        if len(kwd_names) == 3:
            k1 = kwd_names[0]
            k2 = kwd_names[1]
            k3 = kwd_names[2]
    else:
        k1 = input(click.style(" Choose a keyword » ", fg="red", bold=True))
        k2 = input(click.style(" Choose another... » ", fg="red", bold=True))
        k3 = input(click.style(" And another... » ", fg="red", bold=True))

    answers = [titulo, comentario, link, k1, k2, k3]

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
    add()
