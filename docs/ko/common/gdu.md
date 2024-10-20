---
layout: page
title: common/gdu (한국어)
description: "콘솔 인터페이스를 갖춘 디스크 사용량 분석."
content_hash: 18e86d083325c43cc59ccf65fb667624d5c210b4
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/gdu.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/gdu.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gdu.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gdu

콘솔 인터페이스를 갖춘 디스크 사용량 분석.
더 많은 정보: <https://github.com/dundee/gdu>.

- 현재 디렉터리의 디스크 사용량을 대화형으로 표시:

`gdu`

- 주어진 디렉토리의 디스크 사용량을 대화식으로 표시:

`gdu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>

- 마운트된 모든 디스크의 디스크 사용량을 대화형으로 표시:

`gdu --show-disks`

- 현재 디렉터리의 디스크 사용량을 대화형으로 표시하지만, 일부 하위 디렉터리는 무시:

`gdu --ignore-dirs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리1,경로/대상/디렉토리2,...</span>

- 정규식으로 경로를 무시:

`gdu --ignore-dirs-pattern '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.*[abc]+</span>`'`

- 숨겨진 디렉토리는 무시:

`gdu --no-hidden`

- 결과만 출력하고 대화형 모드로 전환하지 않음:

`gdu --non-interactive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>

- 비대화형 모드에선 진행상황을 표시하지 않음 (스크립트에서 유용):

`gdu --no-progress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>
