# crawler-4-cache
Exploring options for preloading nginx server side cache files after a cache purge.
Purpose: speed up site for users for a wordpress website.

Instructions:
Install python and dependent libraries (see code)

***Edit the site map names
***Edit the list of exclusions such as jpg png webp etc

How to Run:
python crawler.py https://site_you_want_to_crawl

Thoughts:
Other methods I've seen used wget to download the entire site then delete the files. Seems like a waste of drive life.

The first crawler I made scanned so deep that it took 100% of the cpu on the server. ouch. Instead of crawling everything - I chose to have it crawl specific site maps.

Much more efficient.

created with the help of AI


