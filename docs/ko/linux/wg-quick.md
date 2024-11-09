---
layout: page
title: linux/wg-quick (한국어)
description: "구성 파일을 기반으로 WireGuard 터널을 빠르게 설정합니다."
content_hash: 43baf444c121face6f09e4bf233cc4c07ac4b5a8
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/wg-quick.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/wg-quick.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># wg-quick

구성 파일을 기반으로 WireGuard 터널을 빠르게 설정합니다.
더 많은 정보: <https://www.wireguard.com/quickstart/>.

- VPN 터널 설정:

`wg-quick up `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스_이름</span>

- VPN 터널 삭제:

`wg-quick down `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스_이름</span>
