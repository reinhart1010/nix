---
layout: page
title: linux/avahi-browse (한국어)
description: "로컬 네트워크에서 mDNS/DNS-SD를 통해 노출된 서비스와 호스트를 표시합니다."
content_hash: 692c5b3040cfe06522d4a657e0b6bec67515168e
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/avahi-browse.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/avahi-browse.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/avahi-browse.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># avahi-browse

로컬 네트워크에서 mDNS/DNS-SD를 통해 노출된 서비스와 호스트를 표시합니다.
Avahi는 Apple 기기에서 발견되는 Bonjour(Zeroconf)와 호환됩니다.
더 많은 정보: <https://www.avahi.org/>.

- 로컬 네트워크에서 사용 가능한 서비스와 해당 주소 및 포트를 나열하되, 로컬 머신의 서비스는 무시:

`avahi-browse --all --resolve --ignore-local`

- 스크립트를 위한 SSV 형식으로 로컬 네트워크의 서비스를 빠르게 나열:

`avahi-browse --all --terminate --parsable`

- 주변 도메인 나열:

`avahi-browse --browse-domains`

- 특정 도메인으로 검색 제한:

`avahi-browse --all --domain=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인</span>
