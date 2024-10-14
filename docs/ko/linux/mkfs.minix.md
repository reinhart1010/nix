---
layout: page
title: linux/mkfs.minix (한국어)
description: "파티션 내에 Minix 파일 시스템 생성."
content_hash: b9e507e4b5ee920a4b1c8d12e489af686b95bcb7
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/linux/mkfs.minix.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/mkfs.minix.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/mkfs.minix.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mkfs.minix

파티션 내에 Minix 파일 시스템 생성.
더 많은 정보: <https://manned.org/mkfs.minix>.

- 장치 b의 파티션 1 (`sdb1`) 에 Minix 파일 시스템 생성:

`mkfs.minix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>
