from __future__ import unicode_literals

import sys

import questionary

from add_mysql import add
from delete_mysql import delete
from search_mysql import search
from see_mysql import see
from update_mysql import update

resposta = questionary.select(
    "What do you want to do?", choices=["Add a Bookmark", "Search for a Bookmark", "See Bookmarks", "Update a Bookmark", "Delete a Bookmark", "Exit"]
).ask()

if resposta == "Add a Bookmark":
    add()
if resposta == "Search for a Bookmark":
    search()
if resposta == "See Bookmarks":
    see()
if resposta == "Update a Bookmark":
    update()
if resposta == "Delete a Bookmark":
    delete()
if resposta == "Exit":
    sys.exit()
