---
layout: page
title: linux/vncviewer (한국어)
description: "VNC (Virtual Network Computing) 클라이언트를 시작합니다."
content_hash: 9624d7eac38083b04efa85d01d6134a6e2f8596d
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/vncviewer.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/vncviewer.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># vncviewer

VNC (Virtual Network Computing) 클라이언트를 시작합니다.
더 많은 정보: <https://manned.org/vncviewer>.

- 지정된 디스플레이의 호스트에 연결하는 VNC 클라이언트 시작:

`vncviewer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디스플레이_번호</span>

- 전체 화면 모드로 시작:

`vncviewer -FullScreen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디스플레이_번호</span>

- 특정 화면 크기로 VNC 클라이언트 시작:

`vncviewer --geometry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">너비</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">높이</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디스플레이_번호</span>

- 지정된 포트의 호스트에 연결하는 VNC 클라이언트 시작:

`vncviewer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>`::`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>
