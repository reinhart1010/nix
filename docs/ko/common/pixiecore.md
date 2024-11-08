---
layout: page
title: common/pixiecore (한국어)
description: "네트워크 부팅을 관리하는 도구."
content_hash: 3987854234372634c17a9076512cc18597dce400
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/pixiecore.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pixiecore

네트워크 부팅을 관리하는 도구.
더 많은 정보: <https://github.com/danderson/netboot/tree/master/pixiecore>.

- `netboot.xyz` 부팅 이미지를 제공하는 PXE 부팅 서버 시작:

`pixiecore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quick</span>` xyz --dhcp-no-bind`

- Ubuntu 부팅 이미지를 제공하는 새로운 PXE 부팅 서버 시작:

`pixiecore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quick</span>` ubuntu --dhcp-no-bind`

- 빠른 모드에서 사용 가능한 모든 부팅 이미지 나열:

`pixiecore quick --help`
