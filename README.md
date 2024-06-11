# Crawler4Cache

Crawler4Cache is a Python script designed to warm the cache of a website by crawling its sitemap and fetching its URLs. This script helps ensure that the cache is preloaded with the necessary content, improving the website's performance and user experience.

## Features

- Fetches URLs from multiple sitemaps.
- Uses concurrent fetching to speed up the cache warming process.
- Logs the progress and any errors encountered during the process.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/finchandchips/crawler-4-cache.git
   cd crawler-4-cache

2. Install Dependencies:
   Install the required Python libraries using pip:

   pip install requests beautifulsoup4

HOW TO USE:

1. Run the Script:

   python crawler4cache.py <main_url>


   Replace <main_url> with the base URL of your website. The script will automatically look for the following sitemaps:

   <main_url>/page-sitemap.xml
   <main_url>/product-sitemap.xml
   <main_url>/post-sitemap.xml

   ***Note: Add or remove sitemaps
   ***This setup I'm using YOAST plugin with WooCommerce

2. Logging:

   The script logs its progress and any errors to cache_warm.log in the same directory.



Example
To run the script for a website with the base URL https://example.com, use the following command:

   python crawler4cache.py https://example.com

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contributing
Feel free to fork this repository and contribute by submitting pull requests. Any contributions are appreciated!

Acknowledgements
Beautiful Soup: A library for parsing HTML and XML documents.
Requests: HTTP for Humans: A simple and elegant HTTP library for Python.

