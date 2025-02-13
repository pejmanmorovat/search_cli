# Google Custom Search CLI Tool

This is a command-line interface (CLI) tool for performing Google Custom Search queries. It allows users to search the web using Google's Custom Search API and view the results directly in the terminal. Users can also open selected search results in their default browser using Termux's `termux-open-url` command.

## Features
- Perform Google searches from the terminal
- Display search results with titles, URLs, and descriptions
- Open selected search results in the browser
- Handle network errors and invalid inputs gracefully

## Requirements
- Python 3.x
- [Requests](https://pypi.org/project/requests/) library for making HTTP requests
- [python-dotenv](https://pypi.org/project/python-dotenv/) for loading environment variables
- [Termux](https://termux.dev/) on Android (or adapt `open_url()` for other systems)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/pejmanmorovat/search_cli.git
    cd search_cli
    ```

2. **Install the required Python packages:**
    ```bash
    pip install requests python-dotenv
    ```

3. **Set up environment variables:**
   - Create a `.env` file in the project directory:
     ```
     GOOGLE_API_KEY=your_google_api_key
     SEARCH_ENGINE_ID=your_search_engine_id
     ```
   - Obtain your Google API Key and Search Engine ID by:
     - Creating a project in the [Google Cloud Console](https://console.cloud.google.com/).
     - Enabling the Custom Search API.
     - Setting up a Custom Search Engine and getting the Search Engine ID.

## Usage

1. **Run the script:**
    ```bash
    python3 search_cli.py
    ```

2. **Enter your search query** and press Enter.

3. **Choose an option:**
   - Enter a result number to open the link in your browser.
   - Enter `back` to return to the search prompt.
   - Enter `quit` to exit the tool.

## Example

```plaintext
Enter search query (or 'quit' to exit): Python programming tutorials

1. Python Documentation
   URL: https://www.python.org/doc/
   Description: Official Python documentation and tutorials.
   ----------------------------------------

2. Learn Python - Free Interactive Python Tutorial
   URL: https://www.learnpython.org/
   Description: An interactive Python tutorial for beginners.
   ----------------------------------------

Enter result number to open (or 'back' for new search): 1
```

ChatGPT

You said:
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

def open_url(url):
    try:
        subprocess.run(['termux-open-url', url])
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
    while True:
        query = input("\nEnter search query (or 'quit' to exit): ")
        if query.lower() == 'quit':
            break
            
        results = perform_search(query)
        if results:
            urls = display_results(results)
            
            while True:
                choice = input("\nEnter result number to open (or 'back' for new search): ")
                if choice.lower() == 'back':
                    break
                try:
                    index = int(choice) - 1
                    if 0 <= index < len(urls):
                        open_url(urls[index])
                    else:
                        print("Invalid result number")
                except ValueError:
                    print("Please enter a valid number")

if __name__ == "__main__":
    main() " write readme file for this code
ChatGPT said:
Google Custom Search CLI Tool
This is a command-line interface (CLI) tool for performing Google Custom Search queries. It allows users to search the web using Google's Custom Search API and view the results directly in the terminal. Users can also open selected search results in their default browser using Termux's termux-open-url command.

Features
Perform Google searches from the terminal
Display search results with titles, URLs, and descriptions
Open selected search results in the browser
Handle network errors and invalid inputs gracefully
Requirements
Python 3.x
Requests library for making HTTP requests
python-dotenv for loading environment variables
Termux on Android (or adapt open_url() for other systems)
Installation
Clone the repository:

git clone https://github.com/your-username/google-search-cli.git
cd google-search-cli
Install the required Python packages:

pip install requests python-dotenv
Set up environment variables:

Create a .env file in the project directory:
GOOGLE_API_KEY=your_google_api_key
SEARCH_ENGINE_ID=your_search_engine_id
Obtain your Google API Key and Search Engine ID by:
Creating a project in the Google Cloud Console.
Enabling the Custom Search API.
Setting up a Custom Search Engine and getting the Search Engine ID.
Usage
Run the script:

python3 search_cli.py
Enter your search query and press Enter.

Choose an option:

Enter a result number to open the link in your browser.
Enter back to return to the search prompt.
Enter quit to exit the tool.
Example
Enter search query (or 'quit' to exit): Python programming tutorials

1. Python Documentation
   URL: https://www.python.org/doc/
   Description: Official Python documentation and tutorials.
   ----------------------------------------

2. Learn Python - Free Interactive Python Tutorial
   URL: https://www.learnpython.org/
   Description: An interactive Python tutorial for beginners.
   ----------------------------------------

Enter result number to open (or 'back' for new search): 1
Error Handling
Empty Query: Prompts the user to enter a valid query.
Invalid Input: Informs the user to enter a valid number or command.
Request Timeout: Displays a timeout message if the request takes too long.
API Errors: Displays relevant error messages for network issues or invalid API keys.
Customization
Modify open_url() if not using Termux:

import webbrowser

def open_url(url):
    webbrowser.open(url)
Change the maximum number of displayed results by modifying the loop in display_results().

Notes
This script is designed for Termux on Android but can be adapted for other environments by modifying the open_url() function.
Ensure the Custom Search API is enabled in your Google Cloud project.
License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

Author
Pejman Morovat

This README provides a comprehensive overview of the Google Custom Search CLI Tool, including installation instructions, usage examples, error handling, and customization tips.






You said:
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
I want add this as file name w3m.py in this repository how to add teadme file and what do i say
ChatGPT said:
To add this as a new file named w3m.py in your existing repository and create an appropriate README section for it, follow these steps:

Step 1: Add the w3m.py File
Navigate to your project directory:

cd google-search-cli
Create and add the w3m.py file:

nano w3m.py
Copy and paste the script into w3m.py, then save and exit.

Stage and commit the new file:

git add w3m.py
git commit -m "Add w3m.py for terminal-based browsing"
git push origin main
Step 2: Update the README File
Open the README.md:

nano README.md
Add the following section:

W3M Browser Integration
The w3m.py script extends the functionality of the Google Custom Search CLI Tool by enabling users to view search results directly in the terminal using the w3m text-based web browser.

Features
Perform Google searches from the terminal
Display search results with titles, URLs, and descriptions
Open selected links in w3m for a text-based browsing experience
Navigate using w3m controls
Requirements
Python 3.x
Requests library for HTTP requests
python-dotenv for environment variables
w3m terminal web browser
Installation
Install w3m (if not already installed):

sudo apt update
sudo apt install w3m




## Author
Pejman Morovat
