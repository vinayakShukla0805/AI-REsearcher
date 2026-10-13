# AI Research Agent

An AI-powered research assistant that searches the web, scrapes the most relevant source, and synthesizes a structured research report with a built-in critic review.

This project combines LLM-driven agents with web search and extraction tools to automate the process of gathering, reading, and summarizing information on a given topic.

## Overview

The application follows a four-step research workflow:

1. Search for recent and relevant sources using Tavily.
2. Pick a strong candidate URL and scrape the page for deeper context.
3. Draft a structured research report using an LLM agent.
4. Critique the generated report and provide improvement feedback.

It exposes both:
- a Streamlit web UI in `app.py`
- a terminal-based pipeline in `pipeline.py`

## Features

- Web search for up-to-date information
- URL scraping for deeper source analysis
- AI-generated structured research reports
- Critic review with strengths, improvement areas, and verdict
- User-friendly Streamlit interface
- Simple modular design with separate agent and tool layers

## Tech Stack

- Python 3.10+
- Streamlit
- LangChain
- Mistral AI (`langchain_mistralai`)
- Tavily Search API
- BeautifulSoup
- Requests
- Python-dotenv

## Project Structure

```text
AI_Reseasrch_Agent/
├── app.py                 # Streamlit user interface
├── agents.py              # LLM agent definitions and prompt chains
├── pipeline.py            # CLI research pipeline runner
├── tools.py               # Tavily search and scraping tools
├── requirement.txt        # Python dependencies
├── .env                   # Local environment variables (API keys)
├── README.md              # Project documentation
└── .gitignore             # Git ignore rules
```

## Environment Setup

1. Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirement.txt
```

3. Add your API keys in a `.env` file:

```env
TAVILY_API_KEY="your_tavily_key"
MISTRAL_API_KEY="your_mistral_key"
```

## Running the Application

### Streamlit web app

```bash
streamlit run app.py
```

This launches the UI where you can enter a research topic and view the search, scraped content, report output, and critique.

### Command-line pipeline

```bash
python pipeline.py
```

The script will prompt for a topic and then run the full research workflow in the terminal.

## How the Workflow Works

The system is organized into a few modular components:

- `tools.py`
  - `web_search(query)`: queries Tavily for recent search results
  - `scrape_url(url)`: fetches and cleans a page's text content

- `agents.py`
  - `build_search_agent()`: agent for finding relevant sources
  - `build_reader_agent()`: agent for selecting and reading a strong source
  - `writer_chain`: generates detailed research reports
  - `critic_chain`: reviews the report and gives structured feedback

- `pipeline.py`
  - orchestrates the full research flow from topic input to final output

## Example Usage

In the Streamlit app, enter a topic such as:

- "Latest trends in generative AI"
- "Impact of EV adoption on urban transportation"
- "Renewable energy storage innovations"

The app will:
- search the web,
- scrape a relevant source,
- generate a polished report,
- provide critique feedback.

## Notes

- This project is designed for research assistance and prototyping, not as a production-grade web crawler.
- Web scraping depends on site accessibility and may fail for pages that block automated requests.
- API keys must be kept private and should not be committed to version control.

## Future Improvements

Potential enhancements include:

- multiple-source aggregation instead of a single scraped source
- citation extraction and source validation
- support for more LLM providers
- PDF/document ingestion
- async multi-agent research execution
- export to Markdown or DOCX

## License

This project is for educational and research purposes.
