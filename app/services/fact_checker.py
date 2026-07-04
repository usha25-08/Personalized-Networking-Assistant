import requests

HEADERS = {
    "User-Agent": "PersonalizedNetworkingAssistant/1.0"
}

def fact_check(query: str):
    try:
        # Search for the most relevant page
        search_url = "https://en.wikipedia.org/w/api.php"

        params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "format": "json"
        }

        search_response = requests.get(
            search_url,
            params=params,
            headers=HEADERS
        )

        search_data = search_response.json()

        results = search_data["query"]["search"]

        if not results:
            return "No reliable information found."

        title = results[0]["title"]

        # Get page summary
        summary_url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + title.replace(" ", "_")

        summary_response = requests.get(
            summary_url,
            headers=HEADERS
        )

        if summary_response.status_code != 200:
            return "No reliable information found."

        summary_data = summary_response.json()

        return summary_data.get("extract", "No reliable information found.")

    except Exception as e:
        return f"Error fetching data: {e}"