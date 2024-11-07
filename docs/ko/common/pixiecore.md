---
layout: page
title: common/pixiecore (한국어)
description: "네트워크 부팅을 관리하는 도구."
content_hash: 3987854234372634c17a9076512cc18597dce400
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/pixiecore.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pixiecore.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pixiecore

네트워크 부팅을 관리하는 도구.
더 많은 정보: <https://github.com/danderson/netboot/tree/master/pixiecore>.

- `netboot.xyz` 부팅 이미지를 제공하는 PXE 부팅 서버 시작:

`pixiecore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quick</span>` xyz --dhcp-no-bind`

- Ubuntu 부팅 이미지를 제공하는 새로운 PXE 부팅 서버 시작:

`pixiecore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quick</span>` ubuntu --dhcp-no-bind`

- 빠른 모드에서 사용 가능한 모든 부팅 이미지 나열:

`pixiecore quick --help`
