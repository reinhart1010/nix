---
layout: page
title: linux/ip-address (한국어)
description: "IP 주소 관리 하위 명령어."
content_hash: 99c814d74eab470196c547667c593db363dd9799
last_modified_at: 2024-11-10
related_topics:
  - title: Deutsch version
    url: /de/linux/ip-address.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/ip-address.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/ip-address.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/ip-address.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ip address

IP 주소 관리 하위 명령어.
더 많은 정보: <https://manned.org/ip-address>.

- 네트워크 인터페이스와 해당 IP 주소 나열:

`ip address`

- 활성 네트워크 인터페이스만 표시하도록 필터링:

`ip address show up`

- 특정 네트워크 인터페이스에 대한 정보 표시:

`ip address show dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- 네트워크 인터페이스에 IP 주소 추가:

`ip address add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_주소</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- 네트워크 인터페이스에서 IP 주소 제거:

`ip address delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_주소</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- 지정된 범위의 모든 IP 주소를 네트워크 인터페이스에서 삭제:

`ip address flush dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` scope `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">global|host|link</span>
