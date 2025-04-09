import sys
import asyncio
from crawl4ai import AsyncWebCrawler

async def main(url):
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=url)
        # Prefer markdown; fall back to HTML if needed.
        if hasattr(result, "markdown") and result.markdown:
            return result.markdown.strip()
        elif hasattr(result, "html") and result.html:
            return result.html.strip()
        else:
            return "No content extracted by Crawl4AI."

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scrape_worker.py <URL>")
    else:
        url = sys.argv[1]
        output = asyncio.run(main(url))
        print(output)