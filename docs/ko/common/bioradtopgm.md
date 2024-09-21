---
layout: page
title: common/bioradtopgm (한국어)
description: "Biorad 공초점 파일을 PGM 파일로 변환."
content_hash: e41927a21f5d3ad91950fae373bd5398ee56907a
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/bioradtopgm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/bioradtopgm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bioradtopgm

Biorad 공초점 파일을 PGM 파일로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/bioradtopgm.html>.

- Biorad 공초점 파일을 읽고 여기에 포함된 n번째 이미지를 PGM 파일로 저장:

`bioradtopgm -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/file.pic</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/file.pgm</span>

- Biorad 공초점 파일을 읽고 포함된 이미지 수를 인쇄:

`bioradtopgm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/file.pic</span>

- 버전 출력:

`bioradtopgm -version`
