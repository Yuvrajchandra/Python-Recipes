import json

languages = {
    "Python" : "Guido van Rossum",
    "C++" : "Bjarne Stroustrup",
    "Java" : "James Gosling"
}

with open("lang.json", "w") as output:
    json.dump(languages, output)
