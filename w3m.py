import os
from dotenv import load_dotenv
import requests
from urllib.parse import quote_plus
import subprocess

# Load environment variables
load_dotenv()

def setup_credentials():
    api_key = os.getenv('GOOGLE_API_KEY')
    search_engine_id = os.getenv('SEARCH_ENGINE_ID')
    
    if not api_key or not search_engine_id:
        raise ValueError("Missing API key or Search Engine ID")
    return api_key, search_engine_id

def open_url_in_w3m(url):
    try:
        subprocess.run(['w3m', url])
    except Exception as e:
        print(f"Error opening URL: {e}")
        print(f"URL: {url}")

def perform_search(query):
    try:
        api_key, search_engine_id = setup_credentials()
        
        if not query.strip():
            raise ValueError("Search query cannot be empty")
        encoded_query = quote_plus(query.strip())
        
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            'q': encoded_query,
            'key': api_key,
            'cx': search_engine_id
        }
        
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
        
    except requests.Timeout:
        print("Request timed out")
    except requests.RequestException as e:
        print(f"Request error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    return None

def display_results(data):
    if not data or 'items' not in data:
        print("No results found")
        return
        
    results = []
    for i, item in enumerate(data['items'], 1):
        print(f"\n{i}. {item['title']}")
        print(f"URL: {item['link']}")
        if 'snippet' in item:
            print(f"Description: {item['snippet']}")
        print("-" * 40)
        results.append(item['link'])
    return results

def main():
    print("\nW3M Browser Controls:")
    print("- Use arrow keys to navigate")
    print("- Press Q to quit and return to search")
    print("- Press H for help with more commands")
    
    while True:
        query = input("\nEnter search query (or 'quit' to exit): ")
        if query.lower() == 'quit':
            break
            
        results = perform_search(query)
        if results:
            urls = display_results(results)
            
            while True:
                choice = input("\nEnter result number to open in w3m (or 'back' for new search): ")
                if choice.lower() == 'back':
                    break
                try:
                    index = int(choice) - 1
                    if 0 <= index < len(urls):
                        open_url_in_w3m(urls[index])
                    else:
                        print("Invalid result number")
                except ValueError:
                    print("Please enter a valid number")

if __name__ == "__main__":
    main()
