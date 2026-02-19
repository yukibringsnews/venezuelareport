import feedparser


# ==============================
# FEED RSS DA MONITORARE
# ==============================

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


# ==============================
# CALCOLO PUNTEGGIO
# ==============================

def relevance_score(title, summary):

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
        "election": 3,
        "opposition": 2
    }

    score = 0

    for k, weight in keywords_weights.items():
        if k in text:
            score += weight

    return score


# ==============================
# FETCH ARTICOLI
# ==============================

def fetch_articles():

    articles = []

    for source, url in RSS_FEEDS.items():

        feed = feedparser.parse(url)

        for entry in feed.entries:

            title = entry.title if "title" in entry else ""
            summary = entry.summary if "summary" in entry else ""
            link = entry.link if "link" in entry else ""

            # gestione data pubblicazione
            if "published" in entry:
                published = entry.published
            else:
                published = ""

            score = relevance_score(title, summary)

            if score >= 5:
                articles.append({
                    "title": title,
                    "summary": summary,
                    "source": source,
                    "link": link,
                    "published": published,
                    "score": score
                })

    articles = sorted(articles, key=lambda x: x["score"], reverse=True)

    return articles
