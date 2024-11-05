---
layout: page
title: common/netdiscover (한국어)
description: "네트워크에서 활성 호스트를 찾기 위한 네트워크 스캐너."
content_hash: 2f55db54e449d6190b52d646d826548d69eab474
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/netdiscover.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/netdiscover.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># netdiscover

네트워크에서 활성 호스트를 찾기 위한 네트워크 스캐너.
더 많은 정보: <https://github.com/netdiscover-scanner/netdiscover>.

- 네트워크 인터페이스의 IP 범위를 스캔하여 활성 호스트 검색:

`netdiscover -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">172.16.6.0/23</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ens244</span>
