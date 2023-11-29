# crawler-4-cache
Crawls the site-maps on a website and opens all of the web pages one at a time. Set a delay to control the speed of the crawl.

Purpose:
Pre-load the server side cache such as nginx fastcgi cache for improved performance for the first visitor.

Instructions:
Install python and dependent libraries (see code)

***Edit the site map names
***Edit the list of exclusions such as jpg png webp etc
***Set time delay to slow down or speed up the process.

How to Run:
python crawler.py https://site_you_want_to_crawl

Thoughts:
Exploring options for preloading nginx server side cache files after a cache purge.

Other methods I've seen used wget to download the entire site then delete the files. Seems like a waste of drive life.

Crawling an entire website uses a lot of resources - the site-maps are updated automatically with all the pages we want to preload.

created with the help of AI


