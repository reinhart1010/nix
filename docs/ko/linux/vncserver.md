---
layout: page
title: linux/vncserver (한국어)
description: "VNC (Virtual Network Computing) 데스크톱 시작."
content_hash: 5801276cea73ad3c5741baffcf2d06275d80092b
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/vncserver.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/vncserver.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># vncserver

VNC (Virtual Network Computing) 데스크톱 시작.
더 많은 정보: <https://manned.org/vncserver.1x>.

- 다음 사용 가능한 디스플레이에 VNC 서버 시작:

`vncserver`

- 특정 화면 크기로 VNC 서버 시작:

`vncserver --geometry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">너비</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">높이</span>

- 특정 디스플레이에서 실행 중인 VNC 서버 인스턴스 종료:

`vncserver --kill :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디스플레이_번호</span>
