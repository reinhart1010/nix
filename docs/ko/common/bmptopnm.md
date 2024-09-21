---
layout: page
title: common/bmptopnm (한국어)
description: "BMP 파일을 PBM, PGM 또는 PNM 이미지로 변환."
content_hash: b1f7e3c9f868370ca0fe8b614823b02c1161a5a2
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/bmptopnm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/bmptopnm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/bmptopnm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bmptopnm

BMP 파일을 PBM, PGM 또는 PNM 이미지로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/bmptopnm.html>.

- Windows 또는 OS/2 BMP 파일의 경우, PBM, PGM 또는 PNM 이미지를 출력으로 생성:

`bmptopnm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/file.bmp</span>

- BMP 헤더의 내용을 `stderr`에 보고:

`bmptopnm -verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/file.bmp</span>

- 버전 표시:

`bmptopnm -version`
