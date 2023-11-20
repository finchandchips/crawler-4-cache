import requests
import webbrowser
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def get_all_links(url, base_website_url):
    response = requests.get(url)
    links = set()

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        base_url = response.url  # Get the base URL after redirects

        for a_tag in soup.find_all('a', href=True):
            link = a_tag['href']

            # Exclude certain URLs
            if (
                link.startswith('javascript:') or
                link.endswith(('.css', '.php', '.jpg')) or
                '#' in link
            ):
                continue

            # Make the URL absolute using the base URL
            absolute_url = urljoin(base_url, link)

            # Check if the absolute URL is from the same domain
            if urlparse(absolute_url).netloc == urlparse(base_website_url).netloc:
                links.add(absolute_url)

    return links

def crawl_website(url):
    # Set of visited links to avoid duplicates
    visited_links = set()

    # Queue for the links to be processed
    link_queue = [url]

    try:
        while link_queue:
            # Get the next link from the queue
            current_link = link_queue.pop(0)

            # Skip if already visited
            if current_link in visited_links:
                continue

            print(f"Crawling: {current_link}")

            # Open the link in the default web browser
            webbrowser.open(current_link, new=0, autoraise=True)  # Open in the same tab

            # Add the current link to the set of visited links
            visited_links.add(current_link)

            # Get all links from the current page
            new_links = get_all_links(current_link, url)

            # Add new links to the queue
            link_queue.extend(new_links)

            # Introduce a shorter delay between requests (adjust as needed)
            time.sleep(0.1)  # Reduced delay to 0.5 seconds

    except KeyboardInterrupt:
        print("Program interrupted by user. Exiting gracefully.")

if __name__ == "__main__":
    # Specify the URL of the website to crawl
    website_url = "##################"

    # Call the crawl_website function
    crawl_website(website_url)
