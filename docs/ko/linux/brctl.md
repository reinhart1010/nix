---
layout: page
title: linux/brctl (한국어)
description: "Ethernet 브리지 관리 도구."
content_hash: b52419fb0fba058a9209adb56f48c8f086a2b5a9
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/brctl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/brctl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/brctl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/brctl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># brctl

Ethernet 브리지 관리 도구.
더 많은 정보: <https://manned.org/brctl>.

- 현재 존재하는 Ethernet 브리지에 대한 정보를 나열:

`sudo brctl show`

- 새 Ethernet 브리지 인터페이스 생성:

`sudo brctl add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브리지_이름</span>

- 기존 Ethernet 브리지 인터페이스 삭제:

`sudo brctl del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브리지_이름</span>

- 기존 브리지에 인터페이스 추가:

`sudo brctl addif `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브리지_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스_이름</span>

- 기존 브리지에서 인터페이스 제거:

`sudo brctl delif `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브리지_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스_이름</span>
