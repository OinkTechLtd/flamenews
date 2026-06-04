import requests
from bs4 import BeautifulSoup
import json
import datetime

SEARCH_SOURCES = ['https://dev.to', 'https://medium.com/feed/tag/technology']

def crawl():
    articles = []
    # Mock crawler logic for demonstration
    headers = {'User-Agent': 'Mozilla/5.0'}
    for url in SEARCH_SOURCES:
        try:
            res = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(res.text, 'html.parser')
            for item in soup.find_all('article')[:5]:
                title = item.find('h2').get_text(strip=True) if item.find('h2') else 'Article'
                link = item.find('a')['href'] if item.find('a') else '#'
                articles.append({
                    'id': str(hash(title)),
                    'title': title,
                    'content': 'This is the extracted content for ' + title + '...', 
                    'date': datetime.datetime.now().isoformat()
                })
        except Exception as e:
            print(f'Error crawling {url}: {e}')
    
    with open('articles.json', 'w') as f:
        json.dump(articles, f)

if __name__ == '__main__':
    crawl()