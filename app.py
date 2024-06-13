import requests
import pandas as pd
import json

def search_google(query, api_key, cse_id):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cse_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve search results. Status code: {response.status_code}")
        return None

def parse_search_results(json_data):
    results = []
    if "items" in json_data:
        for item in json_data["items"]:
            title = item.get('title')
            link = item.get('link')
            results.append((title, link))
            print(f"Found result - Title: {title}, URL: {link}")  # Debugging line
    return results

def generate_queries(parameters):
    primary_categories = parameters["Primary Category"]
    secondary_categories = parameters["Secondary Category"]
    geographies = parameters["Geography"]
    date_ranges = parameters["Date Range"]

    queries = []
    for primary in primary_categories:
        for secondary in secondary_categories:
            for geography in geographies:
                for date_range in date_ranges:
                    query = f"{primary} {secondary} {geography} {date_range}"
                    queries.append(query)
    return queries

def save_to_csv(data, filename='output.csv'):
    if data: 
        df = pd.DataFrame(data, columns=['Title', 'URL'])
        df.to_csv(filename, index=False)
        print(f"Results saved to {filename}")
    else:
        print("No data to save.")

def main(parameters):
    api_key = "CSE_API_KEY"
    cse_id = "CSE_ID"
    
    queries = generate_queries(parameters)
    all_results = []

    for query in queries:
        json_data = search_google(query, api_key, cse_id)
        if json_data:
            results = parse_search_results(json_data)
            all_results.extend(results)
        else:
            print(f"Failed to retrieve search results for query: {query}")
    
    save_to_csv(all_results)

if __name__ == "__main__":

    input_json = '''
    {
        "Primary Category": ["Medical Journal", "Blog", "News"],
        "Secondary Category": ["Orthopedic", "Gynecology"],
        "Geography": ["India", "US", "Europe", "Latin America"],
        "Date Range": ["2022", "2022-23", "Sep 22"]
    }
    '''
    parameters = json.loads(input_json)
    main(parameters)
