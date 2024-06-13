# Web Crawler for Google Search Results

This Python script performs web crawling using the Google Custom Search API to fetch search results based on specified parameters. It retrieves titles and URLs from search results and saves them into a CSV file.

## Prerequisites

- Python 3.x
- Packages listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/monomoy-ok/assignment-2-web-crawler.git
   cd assignment-2-web-crawler
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Configuring Input

Modify the `input_json` variable in `app.py` to specify your search parameters:

```python
input_json = '''
{
    "Primary Category": ["Medical Journal", "Blog", "News"],
    "Secondary Category": ["Orthopedic", "Gynecology"],
    "Geography": ["India", "US", "Europe", "Latin America"],
    "Date Range": ["2022", "2022-23", "Sep 22"]
}
'''
```

### Running the Script

Run the script `app.py`:

```bash
python app.py
```

### Output

The script will fetch search results from Google based on the provided parameters and save them into a CSV file named `output.csv` in the same directory.

## Script Structure

- **`app.py`**: Main script file containing functions for querying Google Search API (`search_google`), parsing results (`parse_search_results`), generating queries (`generate_queries`), and saving results to CSV (`save_to_csv`).


## Acknowledgments

- This script uses the Google Custom Search API for retrieving search results.
- Built with Python, requests, and pandas.


