---
layout: page
title: common/gunzip (한국어)
description: "`gzip` (`.gz`) 아카이브에서 파일을 추출."
content_hash: f1d887a228d517ab43390d06455bd77b5efb80ce
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/gunzip.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gunzip.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gunzip

`gzip` (`.gz`) 아카이브에서 파일을 추출.
더 많은 정보: <https://manned.org/gunzip>.

- 아카이브에서 파일을 추출하고, 원본 파일이 있는 경우 교체:

`gunzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아카이브.tar.gz</span>

- 대상 목적지로 파일을 추출:

`gunzip --stdout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아카이브.tar.gz</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아카이브.tar</span>

- 파일을 추출하고 아카이브 파일을 보관:

`gunzip --keep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아카이브.tar.gz</span>

- 압축 파일의 내용을 나열:

`gunzip --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.txt.gz</span>

- `stdin`에서 아카이브 압축 풀기:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브.gz</span>` | gunzip`
