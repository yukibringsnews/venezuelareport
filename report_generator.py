from collections import Counter
from datetime import datetime


def generate_report(grouped_articles):
    today = datetime.utcnow().strftime("%d %B %Y")

    report = []
    report.append(f"RAPPORTO QUOTIDIANO VENEZUELA")
    report.append(f"Data di redazione: {today}")
    report.append("\n")

    if not grouped_articles:
        report.append("Nessuna informazione rilevante identificata nelle ultime 24 ore.")
        return "\n".join(report)

    for cluster_id, articles in grouped_articles.items():

        report.append("=" * 70)
        report.append("\n")

        # Titolo principale = titolo primo articolo
        main_title = articles[0]["title"]
        report.append(f"TEMA: {main_title}\n")

        sources = [a["source"] for a in articles]
        source_count = Counter(sources)

        report.append("Fonti:")
        for s in source_count:
            report.append(f"- {s}")

        if len(source_count) >= 2:
            report.append("\nVerifica presenza su ≥2 outlet: CONFERMATA")
        else:
            report.append("\nVerifica presenza su ≥2 outlet: riportata da una sola fonte al momento")

        report.append("\nSintesi analitica:\n")

        # Sintesi combinata dei riassunti
        combined_summary = " ".join([a["summary"] for a in articles])

        report.append(combined_summary)

        report.append("\n\nPerché è importante:\n")

        report.append(
            "L’informazione è stata selezionata in quanto rilevante per la "
            "stabilità politica, economica o di sicurezza del Venezuela. "
            "Eventuali conferme multi-fonte rafforzano l’affidabilità del dato. "
            "Qualora la notizia risulti al momento riportata da un solo outlet, "
            "essa viene comunque inclusa per monitoraggio evolutivo nei prossimi giorni."
        )

        report.append("\n\n")

    return "\n".join(report)
