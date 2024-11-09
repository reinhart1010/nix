---
layout: page
title: common/sldtoppm (한국어)
description: "AutoCAD 슬라이드 파일을 PPM 이미지로 변환."
content_hash: 85cacf3c114086afc7bae23865fa7651575b032c
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/sldtoppm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sldtoppm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sldtoppm

AutoCAD 슬라이드 파일을 PPM 이미지로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/sldtoppm.html>.

- SLD 파일을 PPM 이미지로 변환:

`sldtoppm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.sld</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppm</span>

- 비정사각 픽셀을 보정하여 이미지의 너비를 조정:

`sldtoppm -adjust `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.sld</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppm</span>
