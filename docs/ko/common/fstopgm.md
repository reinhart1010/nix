---
layout: page
title: common/fstopgm (한국어)
description: "Usenix FaceSaver 파일을 PGM 이미지로 변환."
content_hash: b353230380b67c0d986f67d8a044cf4bb2da18c3
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/fstopgm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/fstopgm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fstopgm

Usenix FaceSaver 파일을 PGM 이미지로 변환.
참고: `pgmtofs`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/fstopgm.html>.

- 지정된 Usenix FaceSaver 파일을 PGM 이미지로 변환:

`fstopgm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.fs</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pgm</span>
