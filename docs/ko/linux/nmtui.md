---
layout: page
title: linux/nmtui (한국어)
description: "NetworkManager를 제어하기 위한 텍스트 사용자 인터페이스."
content_hash: 7ad4f709f4e4734fbb59bb86b975778eb2b8f352
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/nmtui.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/nmtui.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/nmtui.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/nmtui.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/nmtui.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nmtui

NetworkManager를 제어하기 위한 텍스트 사용자 인터페이스.
화살표 키로 탐색하고, Enter 키로 옵션을 선택하세요.
더 많은 정보: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmtui.html>.

- 사용자 인터페이스 열기:

`nmtui`

- 사용 가능한 연결 목록을 표시하고, 활성화 또는 비활성화 옵션 선택:

`nmtui connect`

- 특정 네트워크에 연결:

`nmtui connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름|UUID|장치|SSID</span>

- 특정 네트워크 편집/추가/삭제:

`nmtui edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름|ID</span>

- 시스템 호스트명 설정:

`nmtui hostname`
