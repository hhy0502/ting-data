import requests
import json
import os

API = "https://static.eudic.net/MediaPool/index.json"

headers = {
    "User-Agent":"Mozilla/5.0"
}

def fetch_articles():

    r = requests.get(API,headers=headers)
    data = r.json()

    result = []

    for item in data[:500]:

        title = item.get("title","")
        mediaid = item.get("id","")

        if not mediaid:
            continue

        result.append({
            "title":title,
            "mediaid":mediaid
        })

    return result


def save_articles(data):

    with open("articles.json","w") as f:
        json.dump(data,f,indent=2)


def main():

    articles = fetch_articles()

    save_articles(articles)

    print("更新文章:",len(articles))


if __name__ == "__main__":
    main()
