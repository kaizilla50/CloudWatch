from datetime import datetime, timezone

from flask import Flask, render_template, request


application = Flask(__name__)


def build_mock_analysis(company_name: str) -> dict:
    normalized_name = company_name.strip()
    lowered = normalized_name.lower()
    score = sum(ord(char) for char in lowered if char.isalnum())

    summaries = [
        "shows steady brand recognition and a clear position in its market.",
        "appears to have consistent customer interest and room for measured growth.",
        "has a recognizable business profile with opportunities to strengthen execution.",
    ]
    risks = [
        "Competition could reduce pricing power and slow growth.",
        "Economic pressure may lower customer spending in key segments.",
        "Operational inefficiencies could affect margins over time.",
    ]
    opportunities = [
        "Expanding digital services could create a stronger recurring revenue base.",
        "Entering adjacent markets may unlock new customer demand.",
        "Improving operational efficiency could support long-term profitability.",
    ]

    return {
        "company_name": normalized_name,
        "summary": f"{normalized_name} {summaries[score % len(summaries)]}",
        "risk": risks[score % len(risks)],
        "opportunity": opportunities[score % len(opportunities)],
    }


@application.route("/", methods=["GET", "POST"])
def index():
    analysis = None
    error_message = None
    company_name = ""

    print(
        f"[{datetime.now(timezone.utc).isoformat()}] "
        f"Received {request.method} request for {request.path}"
    )

    try:
        if request.method == "POST":
            company_name = request.form.get("company_name", "").strip()
            print(
                f"[{datetime.now(timezone.utc).isoformat()}] "
                f"Submitted company name: '{company_name}'"
            )

            if not company_name:
                error_message = "Please enter a company name before submitting."
                print(
                    f"[{datetime.now(timezone.utc).isoformat()}] "
                    "Validation error: empty company name"
                )
            else:
                analysis = build_mock_analysis(company_name)
                print(
                    f"[{datetime.now(timezone.utc).isoformat()}] "
                    f"Generated analysis for '{company_name}'"
                )
    except Exception as exc:
        error_message = "Something went wrong while generating the analysis."
        print(
            f"[{datetime.now(timezone.utc).isoformat()}] "
            f"Application error: {exc}"
        )

    return render_template(
        "index.html",
        analysis=analysis,
        company_name=company_name,
        error_message=error_message,
    )


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000)
