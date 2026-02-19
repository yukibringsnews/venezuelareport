from database import init_db, save_article
from rss_collector import fetch_articles
from clustering import cluster_articles, group_by_cluster
from report_generator import generate_report
from pdf_generator import generate_pdf
from mailer import send_email


def main():

    print("Avvio raccolta articoli...")

    init_db()

    articles = fetch_articles()

    if not articles:
        print("Nessun articolo rilevante trovato.")
        return

    clustered = cluster_articles(articles)
    grouped = group_by_cluster(clustered)

    for article in clustered:
        save_article(article)

    print("Generazione report...")
    report_text = generate_report(grouped)

    pdf_file = generate_pdf(report_text)

    print("Invio email...")
    send_email(
        subject="Rapporto Quotidiano Venezuela",
        body="In allegato il rapporto quotidiano.",
        attachment_path=pdf_file
    )

    print("Operazione completata.")


if __name__ == "__main__":
    main()

