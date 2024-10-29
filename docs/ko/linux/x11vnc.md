---
layout: page
title: linux/x11vnc (한국어)
description: "기존 디스플레이 서버에서 VNC를 활성화하는 VNC 서버."
content_hash: a1bc5cfb0a0c4353fc2f67efed275e8b3c61e8e3
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/linux/x11vnc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/x11vnc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># x11vnc

기존 디스플레이 서버에서 VNC를 활성화하는 VNC 서버.
기본적으로, 서버는 모든 클라이언트가 연결을 끊으면 자동으로 종료됩니다.
더 많은 정보: <https://manned.org/x11vnc>.

- 여러 클라이언트가 연결할 수 있도록 VNC 서버 시작:

`x11vnc -shared`

- 뷰 전용 모드로 VNC 서버를 시작하고 마지막 클라이언트가 연결을 끊어도 종료되지 않도록 설정:

`x11vnc -forever -viewonly`

- 특정 디스플레이와 화면에서 VNC 서버 시작 (둘 다 색인 0부터 시작):

`x11vnc -display :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디스플레이</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">화면</span>

- 세 번째 디스플레이의 기본 화면에서 VNC 서버 시작:

`x11vnc -display :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>

- 첫 번째 디스플레이의 두 번째 화면에서 VNC 서버 시작:

`x11vnc -display :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>
