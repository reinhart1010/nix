---
layout: page
title: linux/sqfscat (한국어)
description: "squashfs 파일 시스템에서 파일을 연결하고 `stdout`에 출력."
content_hash: 48978e2ff5721d6e204e152c4a2c1696a3d7058a
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/sqfscat.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/sqfscat.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/sqfscat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sqfscat

squashfs 파일 시스템에서 파일을 연결하고 `stdout`에 출력.
더 많은 정보: <https://manned.org/sqfscat>.

- squashfs 파일 시스템에서 하나 이상의 파일 내용을 표시:

`sqfscat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_시스템.squashfs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일1 파일2 ...</span>
