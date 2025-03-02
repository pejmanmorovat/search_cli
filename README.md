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

## Error Handling

- **Empty Query:** Prompts the user to enter a valid query.
- **Invalid Input:** Informs the user to enter a valid number or command.
- **Request Timeout:** Displays a timeout message if the request takes too long.
- **API Errors:** Displays relevant error messages for network issues or invalid API keys.

## Customization

- Modify `open_url()` if not using Termux:
  ```python
  import webbrowser

  def open_url(url):
      webbrowser.open(url)
  ```

- Change the maximum number of displayed results by modifying the loop in `display_results()`.

## Notes
- This script is designed for Termux on Android but can be adapted for other environments by modifying the `open_url()` function.
- Ensure the Custom Search API is enabled in your Google Cloud project.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

## Author
Pejman Morovat
To add this as a new file named `w3m.py` in your existing repository and create an appropriate README section for it, follow these steps:

---

## Step 1: Add the `w3m.py` File

1. **Navigate to your project directory**:
    ```bash
    cd google-search-cli
    ```

2. **Create and add the `w3m.py` file**:
    ```bash
    nano w3m.py
    ```

3. **Copy and paste the script into `w3m.py`**, then save and exit.

4. **Stage and commit the new file**:
    ```bash
    git add w3m.py
    git commit -m "Add w3m.py for terminal-based browsing"
    git push origin main
    ```

---

## Step 2: Update the README File

1. **Open the README.md**:
    ```bash
    nano README.md
    ```

2. **Add the following section**:

---

## W3M Browser Integration

The `w3m.py` script extends the functionality of the Google Custom Search CLI Tool by enabling users to view search results directly in the terminal using the `w3m` text-based web browser.

### Features
- Perform Google searches from the terminal
- Display search results with titles, URLs, and descriptions
- Open selected links in `w3m` for a text-based browsing experience
- Navigate using `w3m` controls

### Requirements
- Python 3.x
- [Requests](https://pypi.org/project/requests/) library for HTTP requests
- [python-dotenv](https://pypi.org/project/python-dotenv/) for environment variables
- [w3m](https://packages.debian.org/stable/w3m) terminal web browser

### Installation

1. **Install `w3m`** (if not already installed):
    ```bash
    sudo apt update
    sudo apt install w3m
    ```

2. **Install required Python packages**:
    ```bash
    pip install requests python-dotenv
    ```

3. **Set up environment variables**:
   - Create a `.env` file in the project directory:
     ```
     GOOGLE_API_KEY=your_google_api_key
     SEARCH_ENGINE_ID=your_search_engine_id
     ```

### Usage

1. **Run the script**:
    ```bash
    python3 w3m.py
    ```

2. **Enter your search query** and press Enter.

3. **Choose an option**:
   - Enter a result number to open the link in `w3m`.
   - Enter `back` to return to the search prompt.
   - Enter `quit` to exit the tool.

### Example

```plaintext
Enter search query (or 'quit' to exit): Python tutorials

1. Real Python - Python Tutorials
   URL: https://realpython.com/
   Description: Learn Python programming with tutorials and examples.
   ----------------------------------------

2. Python Documentation
   URL: https://docs.python.org/3/
   Description: Official Python documentation and tutorials.
   ----------------------------------------

Enter result number to open in w3m (or 'back' for new search): 1
```

### W3M Controls
- **Arrow Keys**: Navigate through links
- **Enter**: Open a link
- **Q**: Quit `w3m` and return to the search tool
- **H**: Open help menu for additional commands

### Notes
- This script is designed for Unix-like systems with `w3m` installed.
- Ensure the Custom Search API is enabled in your Google Cloud project.

### License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

---

3. **Save and exit** the editor.

4. **Stage and commit the README changes**:
    ```bash
    git add README.md
    git commit -m "Update README with w3m integration"
    git push origin main
    ```

---

## Step 3: Test the Script

Before sharing the repository, test the script to ensure it works as expected:
```bash
python3 w3m.py
```

Make sure `w3m` opens the URLs correctly, and all commands are functioning smoothly.

---

## Step 4: Share the Repository

Once confirmed, you can share the updated repository link or continue developing additional features!
