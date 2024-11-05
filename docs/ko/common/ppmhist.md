---
layout: page
title: common/ppmhist (한국어)
description: "PPM 이미지에 포함된 색상의 히스토그램을 출력."
content_hash: 0291278bf37905e078b610af374881708f704cbe
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/ppmhist.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ppmhist.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ppmhist

PPM 이미지에 포함된 색상의 히스토그램을 출력.
같이 보기: `pgmhist`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmhist.html>.

- 사람이 읽을 수 있는 형식으로 히스토그램 생성:

`ppmhist -nomap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.ppm</span>

- 이미지의 색상 히스토그램을 주석으로 포함한 컬러맵의 PPM 파일 생성:

`ppmhist -map `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.ppm</span>

- 버전 표시:

`ppmhist -version`
