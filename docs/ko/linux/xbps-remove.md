---
layout: page
title: linux/xbps-remove (한국어)
description: "패키지를 제거하는 XBPS 유틸리티."
content_hash: 0536908c64778c917eceff5fd7605c7d4744e03d
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/xbps-remove.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/xbps-remove.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xbps-remove

패키지를 제거하는 XBPS 유틸리티.
같이 보기: `xbps`.
더 많은 정보: <https://manned.org/xbps-remove.1>.

- 패키지 제거:

`xbps-remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지와 그 의존성 제거:

`xbps-remove --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 고아 패키지 제거 (의존성으로 설치되었지만 더 이상 어떤 패키지도 필요로 하지 않는 패키지):

`xbps-remove --remove-orphans`

- 캐시에서 오래된 패키지 제거:

`xbps-remove --clean-cache`
