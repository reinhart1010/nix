---
layout: page
title: linux/opkg (한국어)
description: "OpenWrt 패키지를 설치하는 데 사용되는 경량 패키지 관리자."
content_hash: 5051d86d9212b279c51fda5c7033ff2aa82db7da
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/opkg.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/opkg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># opkg

OpenWrt 패키지를 설치하는 데 사용되는 경량 패키지 관리자.
더 많은 정보: <https://openwrt.org/docs/guide-user/additional-software/opkg>.

- 패키지 설치:

`opkg install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 제거:

`opkg remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 사용 가능한 패키지 목록 업데이트:

`opkg update`

- 하나 이상의 특정 패키지 업그레이드:

`opkg upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지(들)</span>

- 특정 패키지에 대한 정보 표시:

`opkg info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 사용 가능한 모든 패키지 나열:

`opkg list`
