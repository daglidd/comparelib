import sys
import asyncio
from crawl4ai import AsyncWebCrawler
from firecrawl import Firecrawl

async def main(url):
    # If called with --firecrawl, use Firecrawl
    if '--firecrawl' in sys.argv:
        fc = Firecrawl()
        result = fc.crawl(url)
        if result and 'markdown' in result:
            return result['markdown'].strip()
        elif result and 'html' in result:
            return result['html'].strip()
        else:
            return "No content extracted by Firecrawl."
    else:
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
        print("Usage: python scrape_worker.py <URL> [--firecrawl]")
    else:
        url = sys.argv[1]
        output = asyncio.run(main(url))
        print(output)