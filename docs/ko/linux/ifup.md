---
layout: page
title: linux/ifup (한국어)
description: "네트워크 인터페이스 활성화."
content_hash: f8ef294e75c329fdc283228a085e4d5b697f8807
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/ifup.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/ifup.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/ifup.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ifup

네트워크 인터페이스 활성화.
더 많은 정보: <https://manned.org/ifup.8>.

- 인터페이스 eth0 활성화:

`ifup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- `/etc/network/interfaces`에서 "auto"로 정의된 모든 인터페이스 활성화:

`ifup -a`
