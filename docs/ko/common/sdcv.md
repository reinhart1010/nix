---
layout: page
title: common/sdcv (한국어)
description: "StarDict, 명령줄 사전 클라이언트."
content_hash: 0c6308ec8a39009c277d0da0e88c9265514c0504
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/sdcv.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sdcv.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sdcv

StarDict, 명령줄 사전 클라이언트.
사전은 클라이언트와 별도로 제공됩니다.
더 많은 정보: <https://manned.org/sdcv>.

- `sdcv`를 대화형 모드로 시작:

`sdcv`

- 설치된 사전 나열:

`sdcv --list-dicts`

- 특정 사전에서 정의 표시:

`sdcv --use-dict `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사전_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색어</span>

- 퍼지 검색으로 정의 조회:

`sdcv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색어</span>

- 정확한 검색으로 정의 조회:

`sdcv --exact-search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색어</span>

- 정의를 JSON 형식으로 조회:

`sdcv --json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색어</span>

- 특정 디렉토리에서 사전 검색:

`sdcv --data-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색어</span>
