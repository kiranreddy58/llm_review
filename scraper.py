import requests
from bs4 import BeautifulSoup
import re
import time

def get_reviews(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        req = requests.get(url, headers=headers, timeout=10)
    except:
        return []

    soup = BeautifulSoup(req.text, "html.parser")
    cards = soup.find_all("article", attrs={"data-service-review-card-paper": "true"})

    reviews = []
    
    for c in cards:
        try:
            rating_img = c.find("img", class_=re.compile("starRating", re.I))
            rating = rating_img.get("alt") if rating_img else ""

            author_tag = c.find("span", attrs={"data-consumer-name-typography": "true"})
            author = author_tag.text.strip() if author_tag else ""

            date_tag = c.find("time")
            date = date_tag.text.strip() if date_tag else ""

            paras = c.find_all("p")
            body = paras[0].text.strip() if paras else ""

            heading = c.find(["h2", "h3"])
            title = heading.text.strip() if heading else ""

            text = title + " " + body

            if text.strip():
                reviews.append({
                    "text": text.strip(),
                    "rating": rating,
                    "author": author,
                    "date": date
                })
        except:
            continue

    return reviews
