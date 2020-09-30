"""Create a new file called wiki.py and write a small script that prompts the user for a page title or search phrase
, then prints the summary of that page.
Use a simple loop that continues doing this until the user enters blank input."""

import wikipedia

while True:
    page_title = input("Please enter the page title: ")
    if page_title !="":
        print(wikipedia.search(page_title))
        print(wikipedia.suggest(page_title))
        print(wikipedia.summary(page_title))
    else:
        break