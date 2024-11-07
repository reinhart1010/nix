---
layout: page
title: common/look (한국어)
description: "정렬된 파일에서 특정 접두사로 시작하는 줄을 표시."
content_hash: 03b65d03fe3bde229c08f6750b7aa602ff77e7e1
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/look.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/look.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/look.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># look

정렬된 파일에서 특정 접두사로 시작하는 줄을 표시.
참고: 파일 내의 줄은 정렬되어 있어야 합니다.
같이 보기: `grep`, `sort`.
더 많은 정보: <https://man.openbsd.org/look>.

- 특정 파일에서 특정 접두사로 시작하는 줄 검색:

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">접두사</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 대소문자 구분 없이 ([f]) 영숫자 문자만으로 검색 ([d]):

`look -f -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">접두사</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 문자열 종료 문자 지정 (기본값은 공백):

`look -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,</span>

- `/usr/share/dict/words`에서 검색 (`-d`와 `-f`가 기본적으로 적용됨):

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">접두사</span>
