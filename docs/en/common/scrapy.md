---
layout: page
title: common/scrapy (English)
description: "Web-crawling framework."
content_hash: 7b982f9e5e94fc270b2759a9f0dad45ed521c637
---
# scrapy

Web-crawling framework.
More information: <https://scrapy.org>.

- Create a project:

`scrapy startproject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>

- Create a spider (in project directory):

`scrapy genspider `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">spider_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">website_domain</span>

- Edit spider (in project directory):

`scrapy edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">spider_name</span>

- Run spider (in project directory):

`scrapy crawl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">spider_name</span>

- Fetch a webpage as Scrapy sees it and print the source to stdout:

`scrapy fetch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Open a webpage in the default browser as Scrapy sees it (disable JavaScript for extra fidelity):

`scrapy view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Open Scrapy shell for URL, which allows interaction with the page source in a Python shell (or IPython if available):

`scrapy shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>
