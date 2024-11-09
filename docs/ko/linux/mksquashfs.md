---
layout: page
title: linux/mksquashfs (한국어)
description: "squashfs 파일 시스템에 파일 및 디렉터리를 생성하거나 추가합니다."
content_hash: 28cd87702f4832fec95e8bcd3fa5fda5e6d2e0cf
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/mksquashfs.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/mksquashfs.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/mksquashfs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mksquashfs

squashfs 파일 시스템에 파일 및 디렉터리를 생성하거나 추가합니다.
더 많은 정보: <https://manned.org/mksquashfs>.

- squashfs 파일 시스템에 파일 및 디렉터리를 생성하거나 추가 (`gzip`으로 기본 압축):

`mksquashfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더1 경로/대상/파일_또는_폴더2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일시스템.squashfs</span>

- 특정 [comp]압축 알고리즘을 사용하여 squashfs 파일 시스템에 파일 및 디렉터리를 생성하거나 추가:

`mksquashfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더1 경로/대상/파일_또는_폴더2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일시스템.squashfs</span>` -comp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gzip|lzo|lz4|xz|zstd|lzma</span>

- squashfs 파일 시스템에 파일 및 디렉터리를 생성하거나 추가하면서 일부 제외:

`mksquashfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더1 경로/대상/파일_또는_폴더2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일시스템.squashfs</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_또는_폴더1 파일_또는_폴더2 ...</span>

- gzip으로 끝나는 파일을 제외하고 squashfs 파일 시스템에 파일 및 디렉터리를 생성하거나 추가:

`mksquashfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더1 경로/대상/파일_또는_폴더2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일시스템.squashfs</span>` -wildcards -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.gz</span>`"`

- 정규 표현식과 일치하는 파일을 제외하고 squashfs 파일 시스템에 파일 및 디렉터리를 생성하거나 추가:

`mksquashfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더1 경로/대상/파일_또는_폴더2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일시스템.squashfs</span>` -regex -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>`"`
