import sqlite3
from datetime import datetime

DB_NAME = "venezuela.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            summary TEXT,
            link TEXT,
            source TEXT,
            published TEXT,
            cluster_id INTEGER,
            first_seen TEXT
        )
    ''')

    conn.commit()
    conn.close()

def save_article(article):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute('''
        INSERT INTO articles (title, summary, link, source, published, cluster_id, first_seen)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        article['title'],
        article['summary'],
        article['link'],
        article['source'],
        article['published'],
        article.get('cluster_id'),
        datetime.utcnow().isoformat()
    ))

    conn.commit()
    conn.close()

def get_recent_articles():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute('''
        SELECT title, summary, link, source, published, cluster_id
        FROM articles
        ORDER BY published DESC
        LIMIT 100
    ''')

    rows = c.fetchall()
    conn.close()

    articles = []
    for r in rows:
        articles.append({
            "title": r[0],
            "summary": r[1],
            "link": r[2],
            "source": r[3],
            "published": r[4],
            "cluster_id": r[5]
        })

    return articles
