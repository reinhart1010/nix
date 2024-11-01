---
layout: page
title: common/yuvsplittoppm (한국어)
description: "세 개의 서브샘플링된 Abekas YUV 파일을 하나의 PPM 이미지로 변환."
content_hash: 82cd21917418f90a747830d85889d3ebf5995583
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/yuvsplittoppm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/yuvsplittoppm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># yuvsplittoppm

세 개의 서브샘플링된 Abekas YUV 파일을 하나의 PPM 이미지로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/yuvsplittoppm.html>.

- basename으로 시작하는 세 개의 Akebas YUV 바이트 파일을 읽어 단일 PPM 이미지로 병합하고 지정된 출력 파일에 저장:

`yuvsplittoppm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기본_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">너비</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">높이</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.ppm</span>
