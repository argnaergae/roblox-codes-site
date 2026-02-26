import requests
from bs4 import BeautifulSoup
import json

URL = "https://examplecodesite.com/bloxfruits"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

codes = []

for item in soup.find_all("div", class_="code"):
    codes.append({
        "game": "BloxFruits",
        "code": item.text.strip()
    })

with open("codes.json", "w") as f:
    json.dump(codes, f, indent=2)

print("Updated codes.")
import schedule
import time

schedule.every(30).minutes.do(scrape_function)

while True:
    schedule.run_pending()
    time.sleep(1)
