---
layout: page
title: linux/more (한국어)
description: "파일을 대화형으로 표시하여 스크롤 및 검색을 지원합니다."
content_hash: 40055628619365d322f480e34e31900934908c7a
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/more.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/more.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/more.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># more

파일을 대화형으로 표시하여 스크롤 및 검색을 지원합니다.
같이 보기: `less`.
더 많은 정보: <https://manned.org/more>.

- 파일 열기:

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 줄 표시:

`more +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">줄_번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 다음 페이지로 이동:

`<Space>`

- 문자열 검색 (다음 일치 항목으로 이동하려면 `n` 키 누르기):

`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">무언가</span>

- 종료:

`q`

- 대화형 명령에 대한 도움말 표시:

`h`
