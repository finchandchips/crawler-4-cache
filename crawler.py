import sys
import requests
import webbrowser
import time
from bs4 import BeautifulSoup

def get_urls_from_sitemap(sitemap_url):
    response = requests.get(sitemap_url)

    urls = set()

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'xml')  # Use 'xml' as the parser

        # Extract URLs from the sitemap
        for url_tag in soup.find_all('loc'):
            url = url_tag.text.strip()
            urls.add(url)

    return urls

def is_valid_url(url):
    # Check if the URL ends with common image file extensions
    return not url.endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp'))

def crawl_sitemap(sitemap_url, sitemap_name):
    # Get URLs from the sitemap
    sitemap_urls = get_urls_from_sitemap(sitemap_url)

    # Set of visited links to avoid duplicates
    visited_links = set()

    # Queue for the links to be processed
    link_queue = list(sitemap_urls)

    try:
        while link_queue:
            # Get the next link from the queue
            current_link = link_queue.pop(0)

            # Skip if already visited or URL ends with certain file extensions
            if current_link in visited_links or not is_valid_url(current_link):
                continue

            print(f"Crawling {sitemap_name}: {current_link}")

            # Open the link in the default web browser
            webbrowser.open(current_link, new=0, autoraise=True)  # Open in the same tab

            # Add the current link to the set of visited links
            visited_links.add(current_link)

            # Introduce a delay between requests (adjust as needed)
            time.sleep(1)  # Delay set to 1 seconds

    except KeyboardInterrupt:
        print(f"Program for {sitemap_name} interrupted by user. Exiting gracefully.")

if __name__ == "__main__":
    # Check if the main URL is provided as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <main_url>")
        sys.exit(1)

    main_url = sys.argv[1]

    # Specify the URLs of the sitemaps
    sitemap_url_1 = f"{main_url}/page-sitemap.xml"
    sitemap_url_2 = f"{main_url}/product-sitemap.xml"
    sitemap_url_3 = f"{main_url}/post-sitemap.xml"

    # Call the crawl_sitemap function for the first sitemap
    crawl_sitemap(sitemap_url_1, "Sitemap 1")

    # Call the crawl_sitemap function for the second sitemap
    crawl_sitemap(sitemap_url_2, "Product Sitemap")

    # Call the crawl_sitemap function for the third sitemap
    crawl_sitemap(sitemap_url_3, "Post Sitemap")
