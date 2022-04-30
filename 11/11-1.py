import requests

heroes = ["Hulk", "Captain America", "Thanos"]
best_intelligence = 0
smartest_hero = ""

host = "https://superheroapi.com/api/2619421814940190"

for h in heroes:
    uri = host+f"/search/{h}"
    resp = requests.get(uri).json()
    if resp["response"] == "success":
        id = resp["results"][0]["id"]

        iq = int(resp["results"][0]["powerstats"]["intelligence"])

        if iq > best_intelligence:
            best_intelligence = iq
            smartest_hero = h

print(f"smartest hero is: {smartest_hero}")