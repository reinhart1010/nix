---
layout: page
title: osx/csrutil (한국어)
description: "시스템 무결성 보호 설정 관리."
content_hash: e9077ed66d4f04e1a08b035932ffb25d8a42e213
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/csrutil.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/csrutil.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/csrutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# csrutil

시스템 무결성 보호 설정 관리.
더 많은 정보: <https://keith.github.io/xcode-man-pages/csrutil.8.html>.

- 시스템 무결성 보호 상태 표시:

`csrutil status`

- 시스템 무결성 보호 비활성화:

`csrutil disable`

- 시스템 무결성 보호 활성화:

`csrutil enable`

- 허용된 NetBoot 소스 목록 표시:

`csrutil netboot list`

- 허용된 NetBoot 소스 목록에 IPv4 주소 추가:

`csrutil netboot add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>

- 시스템 무결성 보호 상태 초기화 및 NetBoot 목록 초기화:

`csrutil clear`
