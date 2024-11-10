---
layout: page
title: linux/krfb-virtualmonitor (한국어)
description: "가상 모니터를 생성하고 해당 모니터를 VNC와 함께 사용할 수 있도록 허용합니다."
content_hash: 129a75be74b447e812c5100bc36458cf609ae23d
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/krfb-virtualmonitor.html
    icon: bi bi-globe
tldri18n_status: 2
---
# krfb-virtualmonitor

가상 모니터를 생성하고 해당 모니터를 VNC와 함께 사용할 수 있도록 허용합니다.
더 많은 정보: <https://invent.kde.org/network/krfb>.

- 가상 모니터 생성:

`krfb-virtualmonitor --resolution `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1920</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1080</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모니터_이름</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5900</span>
