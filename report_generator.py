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

    for for cluster_id, articles in grouped_articles.items():

    full_text = " ".join([a["title"] + " " + a["summary"] for a in articles]).lower()

    venezuela_focus = sum(
        1 for a in articles
        if "venezuela" in (a["title"] + " " + a["summary"]).lower()
    )

    if venezuela_focus < len(articles) / 2:
        continue


# Esclude cluster dove Venezuela non è realmente centrale
if "venezuela" not in full_text:
    continue

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
        key_points = []

for a in articles:
    key_points.append(f"- {a['title']} ({a['source']})")

report.append("Elementi chiave emersi:")
for point in key_points:
    report.append(point)

report.append("\nAnalisi sintetica:")

report.append(
    "Le fonti indicano sviluppi rilevanti con impatto potenziale "
    "sulla stabilità politica, economica o di sicurezza del Venezuela. "
    "La convergenza o meno delle fonti suggerisce un diverso grado di consolidamento informativo."
)

        report.append("\n\nPerché è importante:\n")

full_text = " ".join([a["title"] + " " + a["summary"] for a in articles]).lower()

report.append("\nPerché è importante:\n")

if "sanction" in full_text or "oil" in full_text:
    report.append(
        "L’evento ha potenziali implicazioni economiche rilevanti, "
        "in particolare sul settore energetico venezuelano e sul regime sanzionatorio internazionale."
    )

elif "military" in full_text or "us navy" in full_text:
    report.append(
        "L’elemento militare suggerisce un possibile aumento delle tensioni regionali "
        "e un rafforzamento della postura di deterrenza nell’area caraibica."
    )

elif "cartel" in full_text or "narco" in full_text:
    report.append(
        "Il coinvolgimento di attori criminali transnazionali indica rischi "
        "per la sicurezza regionale e possibili implicazioni nei rapporti bilaterali con gli Stati Uniti."
    )

elif "china" in full_text or "russia" in full_text:
    report.append(
        "Il riferimento ad attori extra-regionali segnala un consolidamento "
        "della dimensione geopolitica del dossier venezuelano."
    )

else:
    report.append(
        "L’informazione contribuisce al monitoraggio della stabilità politica interna "
        "e delle dinamiche istituzionali venezuelane."
    )


        report.append("\n\n")

    return "\n".join(report)
