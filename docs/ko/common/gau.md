---
layout: page
title: common/gau (한국어)
description: "모든 URL 가져오기: AlienVault의 Open Threat Exchange, Wayback Machine, 및 모든 도메인에 대한 Common Crawl에서 알려진 URL을 가져옴."
content_hash: 2b368d42bcd5b99891fc0ab406ff20f944fc1b7b
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/gau.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/gau.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gau.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gau

모든 URL 가져오기: AlienVault의 Open Threat Exchange, Wayback Machine, 및 모든 도메인에 대한 Common Crawl에서 알려진 URL을 가져옴.
더 많은 정보: <https://github.com/lc/gau>.

- AlienVault의 Open Threat Exchange, Wayback Machine, Common Crawl 및 URLScan에서 도메인의 모든 URL을 가져옴:

`gau `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 여러 도메인의 URL을 가져옴:

`gau `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인1 도메인2 ...</span>

- 여러 스레드를 실행하여 입력 파일에서 여러 도메인의 모든 URL을 가져옴:

`gau --threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/도메인.txt</span>

- 출력([o]utput) 결과를 파일에 기록:

`gau `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/찾은_주소.txt</span>

- 특정 제공업체의 URL만 검색:

`gau --providers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wayback|commoncrawl|otx|urlscan</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 여러 제공업체의 URL 검색:

`gau --providers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wayback,otx,...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 특정 날짜 범위 내의 URL 검색:

`gau --from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYYMM</span>` --to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYYMM</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>
