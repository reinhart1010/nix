---
layout: page
title: common/ab (中文)
description: "Apache 基准测试工具。"
content_hash: 34399cea5247e4507028d892f059f0d764582d1e
last_modified_at: 2024-06-24
related_topics:
  - title: বাংলা version
    url: /bn/common/ab.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/ab.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ab.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ab.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ab.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ab.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ab.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/ab.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ab.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ab.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/common/ab.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ab.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ab.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/ab.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ab

Apache 基准测试工具。
更多信息：<https://httpd.apache.org/docs/current/programs/ab.html>.

- 向目标 URL 执行 100 次 HTTP GET 请求：

`ab -n 100 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- 使用 10 个并发请求，同时向目标 URL 执行 100 次 HTTP GET 请求：

`ab -n 100 -c 10 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- 使用来自文件的 JSON 负载对 URL 执行 100 个 HTTP POST 请求：

`ab -n 100 -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application/json</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.json</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- 使用 HTTP [K]eep Alive，即在一个 HTTP 会话中执行多个请求：

`ab -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- 为基准测试设置最大的测试时间（单位：秒）：

`ab -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">60</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- 将结果写入到一个 CSV 文件中：

`ab -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.csv</span>
