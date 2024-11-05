---
layout: page
title: common/ppmtoppm (한국어)
description: "PPM 이미지를 복사."
content_hash: 2455af39ea12db8e139c890e0ed4c1338d7021be
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/ppmtoppm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ppmtoppm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ppmtoppm

PPM 이미지를 복사.
더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmtoppm.html>.

- PPM 이미지(즉, PBM, PGM 또는 PPM 이미지)를 `stdin`에서 `stdout`으로 복사:

`ppmtoppm < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppm</span>

- 버전 표시:

`ppmtoppm -version`
