import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import os

BASE_URL = 'https://www.cfos-emobility.de'
START_URL = f'{BASE_URL}/en/cfos-charging-manager/documentation/documentation-links.htm'

REPLACEMENTS = {
    'cFos Charging Manager': 'Snigg Charging Manager',
    'Power Brain Controller': 'Snigg Smart Controller',
    'Power Brain Wallbox': 'Snigg Smart Charger',
    'cFos': 'Snigg',
}

def replace_jargon(text):
    for orig, new in REPLACEMENTS.items():
        text = text.replace(orig, new)
    return text

def fetch_page(url):
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.text

def parse_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select('a')
    urls = []
    for link in links:
        href = link.get('href')
        if href and href.endswith('.htm'):
            full_url = BASE_URL + href if href.startswith('/') else BASE_URL + '/en/cfos-charging-manager/documentation/' + href
            urls.append(full_url)
    return set(urls)

def save_markdown(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    os.makedirs('docs', exist_ok=True)
    main_page = fetch_page(START_URL)
    urls = parse_links(main_page)
    urls.add(START_URL)

    for url in urls:
        print(f'Downloading {url}')
        html = fetch_page(url)
        content = md(html, heading_style='ATX')
        content = replace_jargon(content)
        filename = url.split('/')[-1].replace('.htm', '.md')
        save_markdown(f'docs/{filename}', content)

if __name__ == '__main__':
    main()
