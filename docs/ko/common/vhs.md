---
layout: page
title: common/vhs (한국어)
description: "테이프 파일에서 터미널 GIF 생성."
content_hash: f96c986ea4dccb3414c348cb2492f00e49f328b1
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/vhs.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/vhs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># vhs

테이프 파일에서 터미널 GIF 생성.
더 많은 정보: <https://github.com/charmbracelet/vhs>.

- 테이프 파일 생성 (편집기를 사용하여 테이프 파일에 명령 추가):

`vhs new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.tape</span>

- 테이프 파일에 입력 기록 (완료 후 셸을 종료하여 테이프 생성):

`vhs record > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.tape</span>

- 특정 셸을 사용하여 테이프 파일에 입력 기록:

`vhs record --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">셸</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.tape</span>

- 테이프 파일의 구문 검증:

`vhs validate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.tape</span>

- 테이프 파일에서 GIF 생성:

`vhs < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.tape</span>

- <https://vhs.charm.sh>에 GIF 게시 및 공유 가능한 URL 얻기:

`vhs publish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.gif</span>
