---
layout: page
title: linux/eu-readelf (한국어)
description: "ELF 파일에 대한 정보를 표시합니다."
content_hash: 5c25e0fcb74c8aaf1ecc5ad5dfad24a6fac2295a
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/eu-readelf.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/eu-readelf.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/eu-readelf.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># eu-readelf

ELF 파일에 대한 정보를 표시합니다.
더 많은 정보: <https://manned.org/eu-readelf>.

- ELF 파일에 포함된 모든 추출 가능한 정보 표시:

`eu-readelf --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 모든 NOTE 세그먼트/섹션 또는 특정 세그먼트/섹션의 내용 표시:

`eu-readelf --notes[=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.note.ABI-tag</span>`] `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
