---
layout: page
title: common/scrapy (中文)
description: "Web 爬取框架。"
content_hash: c4e5f8f922bd25c7e3f26be9f0894bab854f0777
last_modified_at: 2024-07-11
related_topics:
  - title: English version
    url: /en/common/scrapy.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/scrapy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# scrapy

Web 爬取框架。
更多信息：<https://scrapy.org>.

- 创建一个项目：

`scrapy startproject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">项目名</span>

- 创建一个爬虫（在项目目录下）：

`scrapy genspider `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">爬虫名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">站点域名</span>

- 编辑爬虫（在项目目录下）：

`scrapy edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">爬虫名</span>

- 运行爬虫（在项目目录下）：

`scrapy crawl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">爬虫名</span>

- 抓取一个网页并将它的网页源码打印至标准输出：

`scrapy fetch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- 使用默认浏览器打开给定的 URL 来确认是否符合期望（为确保准确会禁用 JavaScript）：

`scrapy view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- 通过给定的 URL 打开交互窗口，除此之外还支持 UNIX 风格的本地文件路径：

`scrapy shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>
