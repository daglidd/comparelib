# CompareLib: Web Scraper Comparator

CompareLib is a web application that allows you to compare the output of three different web scraping engines: BeautifulSoup, Crawl4AI, and Firecrawl. Enter a URL and see the extracted content, word counts, and which engine produces the most optimized result.

## Features
- Compare scraping results from BeautifulSoup, Crawl4AI, and Firecrawl
- Modern, responsive frontend (Bootstrap 5)
- Summary section highlights the most optimized (shortest) result
- Dockerized for easy deployment

## Setup

### Prerequisites
- Docker & Docker Compose
- Python 3.10+ (for local development)
- A Firecrawl API key ([get one here](https://docs.firecrawl.dev/))

### Local Development
1. Clone the repo:
   ```sh
   git clone <repo-url>
   cd comparelib
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set your Firecrawl API key as an environment variable:
   ```sh
   export FIRECRAWL_API_KEY=fc-xxxxxx
   ```
4. Run the app:
   ```sh
   python app.py
   ```


### Docker

#### 1. Set your Firecrawl API key
You can set your API key in either `docker-compose.yml` under the `environment:` section, or in a `.env` file in the project root:

**.env example:**
```env
FIRECRAWL_API_KEY=fc-xxxxxx
```

**docker-compose.yml example:**
```yaml
environment:
   - FIRECRAWL_API_KEY=fc-xxxxxx
```

#### 2. Build the Docker image
```sh
docker compose build
```

#### 3. Run the app
```sh
docker compose up
```

#### 4. Access the app
Open your browser and go to [http://localhost:5001](http://localhost:5001)

## Usage
- Enter a website URL in the input box and click "Scrape".
- View and compare the results from all three scrapers.

## License
MIT

---

**Note:**
- You must provide your own Firecrawl API key for Firecrawl results.
- Crawl4AI and Firecrawl may have rate limits or require valid API keys.
