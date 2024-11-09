---
layout: page
title: linux/ip-link (한국어)
description: "네트워크 인터페이스 관리."
content_hash: 33ebe0956e5e777ebf825547fbbb348d20523be8
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/ip-link.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/ip-link.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/ip-link.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ip link

네트워크 인터페이스 관리.
더 많은 정보: <https://manned.org/ip-link>.

- 모든 네트워크 인터페이스 정보 표시:

`ip link`

- 특정 네트워크 인터페이스 정보 표시:

`ip link show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ethN</span>

- 네트워크 인터페이스 활성화 또는 비활성화:

`ip link set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ethN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">up|down</span>

- 네트워크 인터페이스에 의미 있는 이름 부여:

`ip link set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ethN</span>` alias "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">LAN 인터페이스</span>`"`

- 네트워크 인터페이스의 MAC 주소 변경:

`ip link set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ethN</span>` address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ff:ff:ff:ff:ff:ff</span>

- 네트워크 인터페이스의 MTU 크기를 변경하여 점보 프레임 사용:

`ip link set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ethN</span>` mtu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9000</span>
