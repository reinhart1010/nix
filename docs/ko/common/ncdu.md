---
layout: page
title: common/ncdu (한국어)
description: "ncurses 인터페이스를 사용하는 디스크 사용량 분석기."
content_hash: 3c42ad536b3d61694630a4edb8cf52f914fc7ec9
last_modified_at: 2024-11-05
related_topics:
  - title: dansk version
    url: /da/common/ncdu.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ncdu.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ncdu.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ncdu.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ncdu

ncurses 인터페이스를 사용하는 디스크 사용량 분석기.
더 많은 정보: <https://manned.org/ncdu>.

- 현재 작업 중인 디렉터리 분석:

`ncdu`

- 출력에 색상 적용:

`ncdu --color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dark|off</span>

- 지정된 디렉터리 분석:

`ncdu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 결과를 파일에 저장:

`ncdu -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 패턴과 일치하는 파일 제외(추가 패턴을 위해 여러 번 인수 전달 가능):

`ncdu --exclude '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>`'`
