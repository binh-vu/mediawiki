import requests

# req = requests.get("https://en.wikipedia.org/w/api.php?action=parse&page=List of highest mountains on Earth&format=json")

with open("./list-of-highest-mountains-on-earth.txt", "r") as f:
    wikitext = f.read()

req = requests.post(
    # "https://en.wikipedia.org/w/api.php",
    "http://localhost:8080/api.php",
    data={
        "action": "parse",
        "text": wikitext,
        "format": "json",
        "contentmodel": "wikitext",
        "contentformat": "text/x-wiki",
    },
)

try:
    html = req.json()["parse"]["text"]["*"]
except:
    print(req.json())
    raise

with open("base.html", "r") as f:
    template = f.read()
with open("test.html", "w") as f:
    f.write(template.replace("#tt8tty1", html))
    # f.write(html)
