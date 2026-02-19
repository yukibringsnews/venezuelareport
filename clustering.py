from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def cluster_articles(articles, max_clusters=5):
    if not articles:
        return articles

    texts = [a["title"] + " " + a["summary"] for a in articles]

    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(texts)

    # Numero cluster dinamico (mai più dei documenti)
    n_clusters = min(max_clusters, len(articles))

    if n_clusters < 2:
        for a in articles:
            a["cluster_id"] = 0
        return articles

    model = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    labels = model.fit_predict(X)

    for article, label in zip(articles, labels):
        article["cluster_id"] = int(label)

    return articles


def group_by_cluster(articles):
    grouped = {}

    for article in articles:
        cid = article.get("cluster_id", 0)
        if cid not in grouped:
            grouped[cid] = []
        grouped[cid].append(article)

    return grouped
