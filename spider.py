import requests
import json

url = "https://static.eudic.net/MediaPool/index.json"

headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    r = requests.get(url, headers=headers)
    data = r.json()

    articles = []

    for item in data[:100]:
        title = item.get("title","")
        mediaid = item.get("id","")

        articles.append({
            "title": title,
            "mediaid": mediaid
        })

    with open("articles.json","w") as f:
        json.dump(articles,f,indent=2)

    print("抓取完成:",len(articles))

except Exception as e:
    print("错误:",e)
