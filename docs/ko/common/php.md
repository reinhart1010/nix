---
layout: page
title: common/php (한국어)
description: "PHP 명령줄 인터페이스."
content_hash: 71e709a169fc87693d308a4d36772d0c83651e23
last_modified_at: 2024-11-05
related_topics:
  - title: Deutsch version
    url: /de/common/php.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/php.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/php.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/php.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># php

PHP 명령줄 인터페이스.
더 많은 정보: <https://php.net>.

- PHP 스크립트를 구문 분석하고 실행:

`php `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- PHP 스크립트의 문법 검사(즉, 린트):

`php -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- PHP를 대화형으로 실행:

`php -a`

- PHP 코드 실행(참고: `<? ?>` 태그를 사용하지 마세요; 큰따옴표는 백슬래시로 이스케이프하세요):

`php -r "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">코드</span>`"`

- 현재 디렉토리에서 PHP 내장 웹 서버 시작:

`php -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트:포트</span>

- 설치된 PHP 확장 목록:

`php -m`

- 현재 PHP 구성에 대한 정보 표시:

`php -i`

- 특정 함수에 대한 정보 표시:

`php --rf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">함수_이름</span>
