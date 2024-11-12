---
layout: page
title: osx/caffeinate (한국어)
description: "macOS의 절전 모드를 방지합니다."
content_hash: 6d94759d5aed4e042751a5c56a106ac5bc211970
last_modified_at: 2024-11-12
related_topics:
  - title: Deutsch version
    url: /de/osx/caffeinate.html
    icon: bi bi-globe
  - title: English version
    url: /en/osx/caffeinate.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/caffeinate.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/caffeinate.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/caffeinate.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/caffeinate.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/osx/caffeinate.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/caffeinate.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/caffeinate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# caffeinate

macOS의 절전 모드를 방지합니다.
더 많은 정보: <https://keith.github.io/xcode-man-pages/caffeinate.8.html>.

- 1시간(3600초) 동안 절전 모드 방지:

`caffeinate -u -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3600</span>

- 명령이 완료될 때까지 절전 모드 방지:

`caffeinate -s "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>`"`

- 지정된 PID를 가진 프로세스가 완료될 때까지 절전 모드 방지:

`caffeinate -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- 절전 모드 방지 (`Ctrl + C`로 종료):

`caffeinate -i`

- 디스크 절전 모드 방지 (`Ctrl + C`로 종료):

`caffeinate -m`
