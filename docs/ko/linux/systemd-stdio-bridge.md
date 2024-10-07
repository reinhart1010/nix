---
layout: page
title: linux/systemd-stdio-bridge (한국어)
description: "`stdin`/`stdout`와 D-Bus 사이에 프록시를 구현합니다."
content_hash: 9d608fe354668bb9b6dbd2d72b6ad3aba18a4ae6
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/linux/systemd-stdio-bridge.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/systemd-stdio-bridge.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># systemd-stdio-bridge

`stdin`/`stdout`와 D-Bus 사이에 프록시를 구현합니다.
참고: 시작 시 `stdin`/`stdout`을 통해 열린 연결을 수신하도록 되어 있으며, 지정된 버스로 새로운 연결을 생성합니다.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemd-stdio-bridge.html>.

- `stdin`/`stdout`을 로컬 시스템 버스로 전달:

`systemd-stdio-bridge`

- `stdin`/`stdout`을 특정 사용자의 D-Bus로 전달:

`systemd-stdio-bridge --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_명</span>

- 특정 컨테이너 내에서 `stdin`/`stdout`을 로컬 시스템 버스로 전달:

`systemd-stdio-bridge --machine=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mycontainer</span>

- 사용자 지정 D-Bus 주소로 `stdin`/`stdout` 전달:

`systemd-stdio-bridge --bus-path=unix:path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/custom/dbus/socket</span>
