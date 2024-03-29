---
layout: page
title: common/scrapy (English)
description: "Web-crawling framework."
content_hash: d48b6385761bb4afa6c4da8407991a53e478ceab
last_modified_at: 2023-11-12
related_topics:
  - title: 日本語 version
    url: /ja/common/scrapy.html
    icon: bi bi-globe
tldri18n_status: 2
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

- Fetch a webpage as Scrapy sees it and print the source to `stdout`:

`scrapy fetch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Open a webpage in the default browser as Scrapy sees it (disable JavaScript for extra fidelity):

`scrapy view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Open Scrapy shell for URL, which allows interaction with the page source in a Python shell (or IPython if available):

`scrapy shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>
