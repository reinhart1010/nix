---
layout: page
title: linux/addpart (한국어)
description: "지정된 파티션의 존재를 Linux 커널에 알립니다."
content_hash: a78d9e4da0f70f59d95a9efb7e479ee82e6a3ee3
last_modified_at: 2024-11-08
related_topics:
  - title: català version
    url: /ca/linux/addpart.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/addpart.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/addpart.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/addpart.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/addpart.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/addpart.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># addpart

지정된 파티션의 존재를 Linux 커널에 알립니다.
`add partition` ioctl의 간단한 래퍼입니다.
더 많은 정보: <https://manned.org/addpart>.

- 커널에 지정된 파티션의 존재를 알림:

`addpart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장치</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파티션</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시작</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">길이</span>
