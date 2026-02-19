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

def is_relevant(title, summary):
    text = (title + " " + summary).lower()

    mandatory_terms = [
        "venezuela",
        "maduro",
        "caracas",
        "pdvsa"
    ]

    geopolitical_terms = [
        "sanctions",
        "oil",
        "military",
        "cartel",
        "narco",
        "us navy",
        "china",
        "russia",
        "election"
    ]

    # Deve contenere almeno un termine primario
    if not any(term in text for term in mandatory_terms):
        return False

    # E almeno un termine geopolitico rilevante
    if not any(term in text for term in geopolitical_terms):
        return False

    return True


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

                if is_relevant(title, summary):
                    collected.append({
                        "title": title,
                        "summary": summary,
                        "link": link,
                        "source": source,
                        "published": published
                    })

        except Exception as e:
            print(f"Errore fonte: {source} - {e}")

    return collected
