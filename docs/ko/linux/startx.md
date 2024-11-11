---
layout: page
title: linux/startx (한국어)
description: "단일 X 윈도우 시스템 세션 실행을 위한 사용자 인터페이스를 제공하는 `xinit`의 프론트엔드."
content_hash: be9af9103aed423a820436ee07983a858586f58f
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/startx.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/startx.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># startx

단일 X 윈도우 시스템 세션 실행을 위한 사용자 인터페이스를 제공하는 `xinit`의 프론트엔드.
더 많은 정보: <https://x.org/releases/X11R7.5/doc/man/man1/startx.1.html>.

- X 세션 시작:

`startx`

- 미리 정의된 깊이 값으로 X 세션 시작:

`startx -- -depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- 미리 정의된 DPI 값으로 X 세션 시작:

`startx -- -dpi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- `.xinitrc` 파일의 설정을 무시하고 새 X 세션 시작:

`startx /`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/윈도우_매니저_또는_데스크톱_환경</span>
