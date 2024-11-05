---
layout: page
title: common/xzcmp (한국어)
description: "`xz`, `lzma`, `gzip`, `bzip2`, `lzop`, 또는 `zstd`로 압축된 파일을 비교하기 위해 `cmp`를 호출."
content_hash: 86452de1ff0eef4c6da1e2ed6f2c6c1512df78f5
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/xzcmp.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/xzcmp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/xzcmp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xzcmp

`xz`, `lzma`, `gzip`, `bzip2`, `lzop`, 또는 `zstd`로 압축된 파일을 비교하기 위해 `cmp`를 호출.
지정된 모든 옵션은 `cmp`에 직접 전달됨.
더 많은 정보: <https://manned.org/xzcmp>.

- 두 개의 특정 파일 비교:

`xzcmp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2</span>
