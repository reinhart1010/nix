---
layout: page
title: linux/ipcalc (한국어)
description: "IP 주소 및 네트워크에 대한 간단한 연산 및 계산 수행."
content_hash: 22305a74d99a1fd2d242a9098631bcc333b8ef1a
last_modified_at: 2024-11-09
related_topics:
  - title: Deutsch version
    url: /de/linux/ipcalc.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/ipcalc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/ipcalc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ipcalc

IP 주소 및 네트워크에 대한 간단한 연산 및 계산 수행.
더 많은 정보: <https://manned.org/ipcalc>.

- 주어진 서브넷 마스크로 주소 또는 네트워크에 대한 정보 표시:

`ipcalc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.3.4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">255.255.255.0</span>

- CIDR 표기법으로 주소 또는 네트워크에 대한 정보 표시:

`ipcalc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.3.4</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">24</span>

- 주소 또는 네트워크의 브로드캐스트 주소 표시:

`ipcalc -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.3.4</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>

- 제공된 IP 주소와 넷마스크의 네트워크 주소 표시:

`ipcalc -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.3.4</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">24</span>

- 주어진 IP 주소의 지리적 정보 표시:

`ipcalc -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.3.4</span>
