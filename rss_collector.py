import feedparser
from datetime import datetime

# Feed RSS funzionanti e pubblici
RSS_FEEDS = {
    "Reuters World": "https://feeds.reuters.com/Reuters/worldNews",
    "AP News World": "https://apnews.com/hub/world-news?outputType=xml",
    "Al Jazeera": "https://www.aljazeera.com/xml/rss/all.xml",
    "The Guardian World": "https://www.theguardian.com/world/rss",
    "NYT World": "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
    "Washington Post World": "http://feeds.washingtonpost.com/rss/world",
    "Axios World": "https://api.axios.com/feed/world",
    "Brookings": "https://www.brookings.edu/feed/",
    "Council on Foreign Relations": "https://www.cfr.org/rss",
    "Carnegie Endowment": "https://carnegieendowment.org/rss.xml"
}

# Parole chiave Venezuela (ampliabili)
KEYWORDS = [
    "venezuela",
    "maduro",
    "guaido",
    "caracas",
    "pdvsa",
    "cartel",
    "narco",
    "us navy",
    "sanctions",
    "oil",
    "military",
    "china venezuela",
    "russia venezuela"
]

def def relevance_score(title, summary):

    text = (title + " " + summary).lower()

    keywords_weights = {
        "venezuela": 5,
        "maduro": 4,
        "caracas": 4,
        "pdvsa": 5,
        "essequibo": 5,
        "guyana": 3,
        "venezuelan": 4,
        "oil": 2,
        "sanctions": 3,
        "opposition": 2,
        "election": 3
    }

    score = 0

    for k, weight in keywords_weights.items():
        if k in text:
            score += weight

    return score


def fetch_articles():
    collected = []

    for source, url in RSS_FEEDS.items():
        try:
            feed = feedparser.parse(url)

            for entry in feed.entries:
                title = entry.get("title", "")
                summary = entry.get("summary", "")
                link = entry.get("link", "")
                published = entry.get("published", datetime.utcnow().isoformat())

                combined_text = f"{title} {summary}"

                for entry in feed.entries:

    title = entry.title
    summary = entry.summary if "summary" in entry else ""

    score = relevance_score(title, summary)

    if score >= 5:
        articles.append({
            "title": title,
            "summary": summary,
            "source": source,
            "score": score
        })


        except Exception as e:
            print(f"Errore fonte: {source} - {e}")

    return collected
