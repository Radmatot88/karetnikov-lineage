import subprocess
import json
import urllib.parse

titles = "|".join([
    "Куманины",
    "Куманин, Алексей Алексеевич",
    "Куманин, Константин Алексеевич",
    "Куманин, Валентин Алексеевич",
    "Каретниковы",
    "195-й пехотный Оровайский полк",
    "196-й пехотный Инсарский полк",
    "1-й Туркестанский стрелковый полк",
    "Тейково",
    "Зубков, Василий Петрович",
    "Общество соединённых славян"
])

enc = urllib.parse.quote(titles)
url = f"https://ru.wikipedia.org/w/api.php?action=query&titles={enc}&prop=images|pageimages&pithumbsize=1000&format=json"
out = subprocess.check_output(["curl.exe", "-s", "-A", "KaretnikovLineageBot/1.0", url]).decode("utf-8", errors="ignore")
data = json.loads(out)
for k, v in data.get("query", {}).get("pages", {}).items():
    print(f"=== {v.get('title')} ===")
    print("  thumb:", v.get("thumbnail", {}).get("source"))
    imgs = [i["title"] for i in v.get("images", [])]
    print("  images:", imgs)
