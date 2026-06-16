import requests
from datetime import datetime

def generate_log(log_data):
    """
    Accepts a list of log data and writes each item to a file named log_YYYYMMDD.txt.
    Raises ValueError if log_data is not a list.
    """
    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list")

    # Generate filename exactly as log_YYYYMMDD.txt
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Write each item to its own line
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    # Print confirmation message
    print(f"Log written to {filename}")

    # Return the generated filename
    return filename

def fetch_data():
    """
    Fetches data from a specific API endpoint using requests.
    Returns the JSON response if successful, otherwise an empty dictionary.
    """
    url = "https://jsonplaceholder.typicode.com/posts/1"
    try:
        # Use requests.get() as specified
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except Exception:
        pass
    return {}

if __name__ == "__main__":
    # Sample data
    sample_log_data = [
        "User logged in",
        "User updated profile",
        "Report exported"
    ]

    # Call generate_log
    generate_log(sample_log_data)

    # Call fetch_data and print the title
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
