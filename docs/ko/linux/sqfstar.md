---
layout: page
title: linux/sqfstar (한국어)
description: "tar 아카이브에서 squashfs 파일 시스템을 생성합니다."
content_hash: 3cb134947d56447d5a0da448b3a18b5a57f59be8
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/sqfstar.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/sqfstar.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/sqfstar.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sqfstar

tar 아카이브에서 squashfs 파일 시스템을 생성합니다.
더 많은 정보: <https://manned.org/sqfstar>.

- 압축되지 않은 tar 아카이브에서 기본적으로 `gzip`으로 압축된 squashfs 파일 시스템 생성:

`sqfstar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_시스템.squashfs</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아카이브.tar</span>

- `gzip`으로 압축된 tar 아카이브에서 특정 알고리즘으로 파일 시스템을 [comp]압축하여 squashfs 파일 시스템 생성:

`zcat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아카이브.tar.gz</span>` | sqfstar -comp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gzip|lzo|lz4|xz|zstd|lzma</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_시스템.squashfs</span>

- `xz`로 압축된 tar 아카이브에서 일부 파일을 제외하고 squashfs 파일 시스템 생성:

`xzcat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아카이브.tar.xz</span>` | sqfstar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_시스템.squashfs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일1 파일2 ...</span>

- `zstd`로 압축된 tar 아카이브에서 `.gz`로 끝나는 파일을 제외하고 squashfs 파일 시스템 생성:

`zstdcat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아카이브.tar.zst</span>` | sqfstar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_시스템.squashfs</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.gz</span>`"`

- `lz4`로 압축된 tar 아카이브에서 정규 표현식에 맞는 파일을 제외하고 squashfs 파일 시스템 생성:

`lz4cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아카이브.tar.lz4</span>` | sqfstar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_시스템.squashfs</span>` -regex "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>`"`
