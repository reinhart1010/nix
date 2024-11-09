---
layout: page
title: linux/http_load (한국어)
description: "HTTP 벤치마킹 도구."
content_hash: c675dbb28580cbaeb773bf6cf999b58870dde8f4
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/http_load.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/http_load.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># http_load

HTTP 벤치마킹 도구.
웹 서버의 처리량을 테스트하기 위해 여러 HTTP 패치를 병렬로 실행합니다.
더 많은 정보: <https://www.acme.com/software/http_load/>.

- 초당 20개의 요청을 주어진 URL 목록 파일을 기반으로 60초 동안 에뮬레이트:

`http_load -rate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>` -seconds `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">60</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/urls.txt</span>

- 5개의 동시 요청을 주어진 URL 목록 파일을 기반으로 60초 동안 에뮬레이트:

`http_load -parallel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` -seconds `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">60</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/urls.txt</span>

- 초당 20개의 요청으로 1000개의 요청을 주어진 URL 목록 파일을 기반으로 에뮬레이트:

`http_load -rate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>` -fetches `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1000</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/urls.txt</span>

- 5개의 동시 요청으로 1000개의 요청을 주어진 URL 목록 파일을 기반으로 에뮬레이트:

`http_load -parallel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` -fetches `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1000</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/urls.txt</span>
