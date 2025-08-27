import asyncio
import subprocess
import requests
from bs4 import BeautifulSoup
from firecrawl import Firecrawl
import os
from flask import Flask, request, render_template

app = Flask(__name__)

def scrape_with_bs4(url: str) -> str:
    """Scrape using requests and BeautifulSoup."""
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup.prettify()
        else:
            return f"Error: Received status code {response.status_code}"
    except Exception as exc:
        return f"Error: {exc}"

def scrape_with_crawl4ai(url: str) -> str:
    """Scrape using Crawl4AI via a dedicated subprocess."""
    try:
        result = subprocess.check_output(
            ["python", "scrape_worker.py", url],
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            timeout=60
        )
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}"
    except Exception as exc:
        return f"Error: {exc}"

def scrape_with_firecrawl(url: str) -> str:
    """Scrape using Firecrawl directly."""
    try:
        api_key = os.environ.get("FIRECRAWL_API_KEY")
        if not api_key:
            return "Error: Firecrawl API key not set."
        url_api = "https://api.firecrawl.dev/v2/scrape"
        payload = {
            "url": url,
            "onlyMainContent": True,
            "maxAge": 172800000,
            "parsers": ["pdf"],
            "formats": ["markdown"]
        }
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        response = requests.post(url_api, json=payload, headers=headers)
        data = response.json()
        if data.get("success") and "data" in data and "markdown" in data["data"]:
            return data["data"]["markdown"].strip()
        else:
            return "No content extracted by Firecrawl."
    except Exception as exc:
        return f"Error: {exc}"

@app.route("/", methods=["GET", "POST"])
def index():
    bs4_result = ""
    crawl4ai_result = ""
    firecrawl_result = ""
    url = ""
    if request.method == "POST":
        url = request.form.get("url", "")
        if url:
            bs4_result = scrape_with_bs4(url)
            crawl4ai_result = scrape_with_crawl4ai(url)
            firecrawl_result = scrape_with_firecrawl(url)
    return render_template("index.html", url=url, bs4_result=bs4_result, crawl4ai_result=crawl4ai_result, firecrawl_result=firecrawl_result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)