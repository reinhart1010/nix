---
layout: page
title: common/netdiscover (한국어)
description: "네트워크에서 활성 호스트를 찾기 위한 네트워크 스캐너."
content_hash: 2f55db54e449d6190b52d646d826548d69eab474
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/netdiscover.html
    icon: bi bi-globe
tldri18n_status: 2
---
# netdiscover

네트워크에서 활성 호스트를 찾기 위한 네트워크 스캐너.
더 많은 정보: <https://github.com/netdiscover-scanner/netdiscover>.

- 네트워크 인터페이스의 IP 범위를 스캔하여 활성 호스트 검색:

`netdiscover -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">172.16.6.0/23</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ens244</span>
