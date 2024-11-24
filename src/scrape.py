# Get the top 5 headlines from the BBC news website

import urllib.request
from bs4 import BeautifulSoup

def get_headlines():
    url = "https://www.bbc.co.uk/news"

    with urllib.request.urlopen(url) as reponse:
        html = reponse.read()

    soup = BeautifulSoup(html, 'html.parser')
    aria_hidden_span = soup.find_all('span', {'aria-hidden': 'false'})
    headlines = [span.get_text(strip=True) for span in aria_hidden_span]
    top_5_headlines = headlines[:5]

    return top_5_headlines