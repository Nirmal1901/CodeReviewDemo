import requests
from bs4 import BeautifulSoup

def get_links_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')
    return [link.get('href') for link in links]

# Example usage:
# links = get_links_from_url('https://example.com')
