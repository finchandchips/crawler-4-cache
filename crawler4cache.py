import sys
import requests
import time
import logging
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed

# Set up logging configuration
logging.basicConfig(filename='cache_warm.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def get_urls_from_sitemap(sitemap_url):
    """
    Fetches URLs from the given sitemap URL.

    Args:
        sitemap_url (str): URL of the sitemap to fetch URLs from.

    Returns:
        set: A set of URLs extracted from the sitemap.
    """
    try:
        response = requests.get(sitemap_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        urls = set()
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'xml')  # Use 'xml' as the parser
            for url_tag in soup.find_all('loc'):
                url = url_tag.text.strip()
                urls.add(url)
        return urls
    except requests.RequestException as e:
        logging.error(f"Error fetching sitemap {sitemap_url}: {e}")
        return set()

def is_valid_url(url):
    """
    Checks if the URL is valid for caching (not an image file).

    Args:
        url (str): URL to check.

    Returns:
        bool: True if the URL is valid, False otherwise.
    """
    # Check if the URL ends with common image file extensions
    return not url.endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp'))

def fetch_url(url):
    """
    Fetches the content of the URL to warm the cache.

    Args:
        url (str): URL to fetch.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        logging.info(f"Fetched URL: {url}")
    except requests.RequestException as e:
        logging.error(f"Error fetching URL {url}: {e}")

def crawl_sitemap(sitemap_url, sitemap_name):
    """
    Crawls the given sitemap and warms the cache for each URL.

    Args:
        sitemap_url (str): URL of the sitemap to crawl.
        sitemap_name (str): Name of the sitemap (for logging purposes).
    """
    sitemap_urls = get_urls_from_sitemap(sitemap_url)
    valid_urls = [url for url in sitemap_urls if is_valid_url(url)]
    
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(fetch_url, url) for url in valid_urls]
        for future in as_completed(futures):
            future.result()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <main_url>")
        sys.exit(1)

    main_url = sys.argv[1]

    # Define the sitemap URLs
    sitemap_url_1 = f"{main_url}/page-sitemap.xml"
    sitemap_url_2 = f"{main_url}/product-sitemap.xml"
    sitemap_url_3 = f"{main_url}/post-sitemap.xml"

    # Crawl each sitemap
    crawl_sitemap(sitemap_url_1, "Sitemap 1")
    crawl_sitemap(sitemap_url_2, "Product Sitemap")
    crawl_sitemap(sitemap_url_3, "Post Sitemap")
