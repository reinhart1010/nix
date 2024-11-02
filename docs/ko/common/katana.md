---
layout: page
title: common/katana (한국어)
description: "자동화 파이프라인에서의 실행에 중점을 둔 빠른 크롤러로, 헤드리스 및 비헤드리스 크롤링을 모두 제공합니다."
content_hash: a41f7ad60e0f1b3a7bb5b02702afb19799ac8e12
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/katana.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/katana.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># katana

자동화 파이프라인에서의 실행에 중점을 둔 빠른 크롤러로, 헤드리스 및 비헤드리스 크롤링을 모두 제공합니다.
같이 보기: `gau`, `scrapy`, `waymore`.
더 많은 정보: <https://github.com/projectdiscovery/katana>.

- URL 목록을 크롤링:

`katana -list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com,https://google.com,...</span>

- Chromium을 사용하여 헤드리스 모드로 URL 크롤링:

`katana -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>` -headless`

- `subfinder`를 사용하여 서브도메인을 찾고, [p]a[s]sive 소스(Wayback Machine, Common Crawl, AlienVault)로 URL 검색:

`subfinder -list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/domains.txt</span>` | katana -passive`

- 프록시(http/socks5)를 통해 요청 전달하고 파일에서 사용자 정의 [H]eaders 사용:

`katana -proxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://127.0.0.1:8080</span>` -headers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/headers.txt</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- 크롤링 [s]trategy, 크롤링할 하위 디렉토리의 [d]epth, 속도 제한(초당 요청 수) 지정:

`katana -strategy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">depth-first|breadth-first</span>` -depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>` -rate-limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- `subfinder`를 사용하여 서브도메인을 찾고, 각 서브도메인을 최대 시간 동안 크롤링하며 결과를 [o]utput 파일에 저장:

`subfinder -list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/domains.txt</span>` | katana -crawl-duration `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>` -output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/output.txt</span>
