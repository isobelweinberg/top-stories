import requests

# URL of the BBC News homepage
url = "https://www.bbc.com/news"

# Send a GET request to fetch the HTML content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    html_content = response.text
    with open("tests/bbc_homepage.html", "w", encoding="utf-8") as file:
        file.write(html_content)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
