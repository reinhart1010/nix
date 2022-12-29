---
layout: page
title: common/bzip2 (한국어)
description: "블록 정렬 파일 압축기."
content_hash: 3e738b77980a97970721b39c83eb16cc8a65dfa4
last_modified_at: 2022-12-29
related_topics:
  - title: English version
    url: /en/common/bzip2.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bzip2.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/bzip2.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/bzip2.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bzip2

블록 정렬 파일 압축기.
더 많은 정보: <https://manned.org/bzip2>.

- 파일 압축하기:

`bzip2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/압축할_파일명</span>

- 파일 압축해제하기:

`bzip2 -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/압축된_.bz2파일</span>

- 파일을 표준 출력으로 압축해제:

`bzip2 -dc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/압축된_.bz2파일</span>
