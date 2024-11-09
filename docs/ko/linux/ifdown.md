---
layout: page
title: linux/ifdown (한국어)
description: "네트워크 인터페이스 비활성화."
content_hash: 6eaf4477ab04535b7cc4258e6d4d09ee1ac0365c
last_modified_at: 2024-11-09
related_topics:
  - title: català version
    url: /ca/linux/ifdown.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/ifdown.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/ifdown.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/ifdown.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/ifdown.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/ifdown.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ifdown

네트워크 인터페이스 비활성화.
더 많은 정보: <https://manned.org/ifdown>.

- 인터페이스 eth0 비활성화:

`ifdown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- 활성화된 모든 인터페이스 비활성화:

`ifdown -a`
