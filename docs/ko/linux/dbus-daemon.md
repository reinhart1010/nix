---
layout: page
title: linux/dbus-daemon (한국어)
description: "여러 프로그램이 메시지를 교환할 수 있도록 하는 D-Bus 메시지 데몬."
content_hash: 6b395801abd9aea2ce9285be5e9f46980107b6d3
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/dbus-daemon.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dbus-daemon.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dbus-daemon

여러 프로그램이 메시지를 교환할 수 있도록 하는 D-Bus 메시지 데몬.
더 많은 정보: <https://www.freedesktop.org/wiki/Software/dbus/>.

- 구성 파일을 사용하여 데몬 실행:

`dbus-daemon --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 표준 로그인 세션당 메시지 버스 구성으로 데몬 실행:

`dbus-daemon --session`

- 표준 시스템 전체 메시지 버스 구성으로 데몬 실행:

`dbus-daemon --system`

- 수신할 주소 설정 및 해당 구성 값 재정의:

`dbus-daemon --address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주소</span>

- 프로세스 ID를 `stdout`에 출력:

`dbus-daemon --print-pid`

- 메시지를 시스템 로그에 기록하도록 메시지 버스를 강제 설정:

`dbus-daemon --syslog`
