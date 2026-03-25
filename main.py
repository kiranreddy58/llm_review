import pandas as pd
from scraper import get_reviews
from preprocess import clean, chunk_text
from llm import summarize

def main():
    print("Trustpilot Review Summarizer")
    print("-" * 30)
    
    url = ""
    while len(url) == 0:
        url = input("Enter Trustpilot product URL: ").strip().strip("`'\"")

    if not url.startswith("http"):
        url = "https://" + url

    print("\nFetching reviews...")
    reviews = get_reviews(url)

    if len(reviews) == 0:
        print("No reviews found or page blocked.")
        return

    print("Found", len(reviews), "reviews. Processing with LLM...")

    data = []
    for r in reviews:
        print("Processing review by", r["author"])
        
        txt = clean(r["text"])
        parts = chunk_text(txt)

        final_sum = ""
        for p in parts:
            res = summarize(p)
            final_sum += res + " "

        data.append({
            "author": r["author"],
            "date": r["date"],
            "rating": r["rating"],
            "review": txt,
            "summary": final_sum.strip()
        })

    df = pd.DataFrame(data)
    df.to_csv("output.csv", index=False)
    print("\nDone! Results saved to output.csv")

if __name__ == "__main__":
    main()
