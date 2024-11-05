---
layout: page
title: common/xteddy (한국어)
description: "X Windows 데스크탑에 귀여운 곰 인형을 표시하는 도구."
content_hash: 01dc265c6437f8fa28a90e2f6a8ceb1f65c9739a
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/xteddy.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/xteddy.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xteddy

X Windows 데스크탑에 귀여운 곰 인형을 표시하는 도구.
더 많은 정보: <https://manned.org/xteddy.1>.

- X 데스크탑에 귀여운 곰 인형 표시:

`xteddy`

- 윈도우 매니저를 사용해 곰 인형을 표시하고 "종료" (`q`) 명령을 무시:

`xteddy -wm -noquit`

- 곰 인형이 다른 모든 창 위에 머물도록 설정:

`xteddy -float`

- 귀여운 곰 인형 대신 다른 이미지 [F] 파일 표시:

`xteddy -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지</span>

- 곰 인형의 초기 위치 설정 (`너비` 및 `높이`는 무시됨):

`xteddy -geometry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">너비</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">높이</span>`+`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x</span>`+`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y</span>
