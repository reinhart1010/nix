---
layout: page
title: common/tgatoppm (한국어)
description: "TrueVision Targa 파일을 Netpbm 이미지로 변환."
content_hash: 4cb1c210899e45a5121683081d0335831fb4f5ed
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/tgatoppm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tgatoppm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tgatoppm

TrueVision Targa 파일을 Netpbm 이미지로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/tgatoppm.html>.

- TrueVision Targa 파일을 PPM 이미지로 변환:

`tgatoppm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.tga</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppm</span>

- TGA 헤더의 정보를 `stdout`로 덤프:

`tgatoppm --headerdump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.tga</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppm</span>

- 입력 이미지의 투명 채널 값을 지정한 파일에 작성:

`tgatoppm --alphaout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/투명도_파일.pgm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.tga</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppm</span>

- 버전 표시:

`tgatoppm -version`
