---
layout: page
title: linux/mate-search-tool (한국어)
description: "MATE 데스크톱 환경에서 파일 검색."
content_hash: 463eb11e0e30112dfa62ed9ba496f361ce1108f6
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/mate-search-tool.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/mate-search-tool.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mate-search-tool

MATE 데스크톱 환경에서 파일 검색.
더 많은 정보: <https://manned.org/mate-search-tool>.

- 특정 디렉토리에서 이름에 특정 문자열이 포함된 파일 검색:

`mate-search-tool --named=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>` --path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 사용자 확인을 기다리지 않고 파일 검색:

`mate-search-tool --start --named=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>` --path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 특정 정규 표현식과 일치하는 이름의 파일 검색:

`mate-search-tool --start --regex=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>` --path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 검색 결과 정렬 순서 설정:

`mate-search-tool --start --named=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>` --path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --sortby=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|folder|size|type|date</span>

- 내림차순 정렬 설정:

`mate-search-tool --start --named=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>` --path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --descending`

- 특정 사용자/그룹 소유의 파일 검색:

`mate-search-tool --start --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user|group</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>` --path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
