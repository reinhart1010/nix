---
layout: page
title: osx/dmesg (한국어)
description: "커널 메시지를 `stdout`에 출력합니다."
content_hash: 88a7277e629b9cc08859b52ae539fe37689db77c
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/dmesg.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/dmesg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/dmesg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/dmesg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dmesg

커널 메시지를 `stdout`에 출력합니다.
더 많은 정보: <https://keith.github.io/xcode-man-pages/dmesg.8.html>.

- 커널 메시지 표시:

`dmesg`

- 이 시스템에서 사용 가능한 물리적 메모리 양 표시:

`dmesg | grep -i memory`

- 한 번에 한 페이지씩 커널 메시지 표시:

`dmesg | less`
