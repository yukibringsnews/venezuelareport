from collections import Counter
from datetime import datetime


def generate_report(grouped_articles):
    from collections import Counter
from datetime import datetime


def generate_report(grouped_articles):

    today = datetime.utcnow().strftime("%d %B %Y")

    report = []
    report.append("RAPPORTO QUOTIDIANO VENEZUELA")
    report.append(f"Data di redazione: {today}")
    report.append("\n")

    if not grouped_articles:
        report.append("Nessuna informazione rilevante identificata.")
        return "\n".join(report)

    for cluster_id, articles in grouped_articles.items():

        full_text = " ".join(
            [a["title"] + " " + a["summary"] for a in articles]
        ).lower()

        venezuela_focus = sum(
            1 for a in articles
            if "venezuela" in (a["title"] + " " + a["summary"]).lower()
        )

        if venezuela_focus < len(articles) / 2:
            continue

        report.append("=" * 70)
        report.append("\n")

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

        report.append("\nElementi chiave emersi:")
        for a in articles:
            report.append(f"- {a['title']} ({a['source']})")

        report.append("\nPerché è importante:\n")

        if "sanction" in full_text or "oil" in full_text:
            report.append(
                "L’evento ha implicazioni economiche rilevanti sul settore energetico venezuelano."
            )
        elif "military" in full_text:
            report.append(
                "Il riferimento militare suggerisce possibili tensioni regionali."
            )
        elif "cartel" in full_text or "narco" in full_text:
            report.append(
                "Il coinvolgimento di reti criminali indica rischi per la sicurezza regionale."
            )
        elif "china" in full_text or "russia" in full_text:
            report.append(
                "Il coinvolgimento di attori extra-regionali rafforza la dimensione geopolitica del dossier."
            )
        else:
            report.append(
                "L’informazione contribuisce al monitoraggio della stabilità politica interna."
            )

        report.append("\n\n")

    return "\n".join(report)
