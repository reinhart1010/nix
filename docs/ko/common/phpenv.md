---
layout: page
title: common/phpenv (한국어)
description: "개발 목적을 위한 PHP 버전 관리자."
content_hash: 70cc651e8d35056668bfd5273f72c62d5d01717d
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/phpenv.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/phpenv.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># phpenv

개발 목적을 위한 PHP 버전 관리자.
더 많은 정보: <https://github.com/phpenv/phpenv>.

- PHP 버전을 전역으로 설치:

`phpenv install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- `phpenv`에 알려진 모든 PHP 바이너리에 대한 shim 파일 새로 고침:

`phpenv rehash`

- 설치된 모든 PHP 버전 나열:

`phpenv versions`

- 현재 활성화된 PHP 버전 표시:

`phpenv version`

- 전역 PHP 버전 설정:

`phpenv global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 로컬 PHP 버전 설정 (전역 버전보다 우선):

`phpenv local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 로컬 PHP 버전 해제:

`phpenv local --unset`
