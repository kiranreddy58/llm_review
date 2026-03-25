# LLM Product Review Summarizer

This is a Python script that scrapes product reviews from Trustpilot, chunks the text by tokens, and sends it to the Groq API to get a sentiment and summary for each review. Finally, it saves everything into a CSV file.

## Setup

First, make sure you have python installed. Then download the code and run:

```bash
pip install -r requirements.txt
```

You will need a free API key from [Groq](https://console.groq.com). Open the project folder, create a file named `.env`, and paste your key inside like this:

```
GROQ_API_KEY=your_key_here
```

## How to use it

Run the main file:

```bash
python main.py
```

It will ask you for a product review URL. You can paste any Trustpilot review page. 

**Example URL:**
`https://www.trustpilot.com/review/www.bestbuy.com`

The script will scrape the reviews, send them to the API, and create an `output.csv` file in the same folder with the results.

## Notes
- I used Trustpilot because direct sites like Amazon or Best Buy block scrapers with CAPTCHAs, but Trustpilot allows simple HTTP requests to scrape real product reviews.
- I used `tiktoken` to count tokens before sending data to the LLM to make sure long reviews don't break the API limit.
- The default model is `llama-3.3-70b-versatile` but you can change it in the code.

## Output video for the assignment

<video width="100%" controls>
  <source src="Sequence 01.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
