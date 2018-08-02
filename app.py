import json
from difflib import get_close_matches


data = json.load(open("data.json", "r"))


def translate(word):
    try:
        return data[word.lower()]
    except KeyError:
        if word.title() in data:
            return data[word.title()]
        elif word.upper() in data:
            return data[word.upper()]
        else:
            suggestion = get_close_matches(word, data.keys(), cutoff=0.8)
            if len(suggestion) >= 1:
                ask = input("we cant find that word, would you like to try with the word: %s ?"
                            " write 'y' for yes or 'n' for no" % suggestion[0])
                if ask == "y":
                    return translate(suggestion[0])
                elif ask == "n":
                    return "Try again with a new word"
                else:
                    "Sorry, We did not understand your input"
            else:
                return "Word not found. Please try again"


search = input("search for:")

while search != "exit":
    results = translate(search)
    if type(results) == list:
        for definition in results:
            print(definition)
    else:
        print(results)

    search = input("Enter a new Word or write exit to finish process:")