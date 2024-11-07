---
layout: page
title: common/pickle (한국어)
description: "Composer 기반의 PHP 확장 프로그램 설치 도구."
content_hash: 45f85770a8018b14d3c06c8f81f283897fb0522e
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/pickle.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pickle.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pickle

Composer 기반의 PHP 확장 프로그램 설치 도구.
더 많은 정보: <https://github.com/FriendsOfPHP/pickle>.

- 특정 PHP 확장 프로그램 설치:

`pickle install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">확장_이름</span>

- 기존 PECL 확장 구성 파일을 Pickle 구성 파일로 변환:

`pickle convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- PECL 확장 유효성 검사:

`pickle validate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- PECL 확장을 릴리스용으로 패키징:

`pickle release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
