---
layout: page
title: linux/xterm (한국어)
description: "X 윈도우 시스템용 터미널 에뮬레이터."
content_hash: 0908334ccff7a148228a93bf65bfd150a9abad09
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/linux/xterm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/xterm.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/xterm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/xterm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xterm

X 윈도우 시스템용 터미널 에뮬레이터.
더 많은 정보: <https://manned.org/xterm>.

- `Example`이라는 제목으로 터미널 열기:

`xterm -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Example</span>

- 전체 화면 모드로 터미널 열기:

`xterm -fullscreen`

- 어두운 파란색 배경과 노란색 전경(글꼴 색상)으로 터미널 열기:

`xterm -bg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">darkblue</span>` -fg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yellow</span>

- 각 줄에 100자, 35줄로, 화면 위치 x=200px, y=20px에 터미널 열기:

`xterm -geometry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">35</span>`+`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">200</span>`+`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>

- Serif 글꼴과 글꼴 크기 20으로 터미널 열기:

`xterm -fa `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'Serif'</span>` -fs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>
