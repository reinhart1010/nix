---
layout: page
title: common/ppmtoascii (한국어)
description: "PPM 이미지를 ANSI 터미널 색상 코드를 사용하여 ASCII 이미지로 변환."
content_hash: b38d0d49fe221f8b45f3419325e3ad94510ecb5b
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/ppmtoascii.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ppmtoascii.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ppmtoascii

PPM 이미지를 ANSI 터미널 색상 코드를 사용하여 ASCII 이미지로 변환.
같이 보기: `ppmtoterm`, `pbmtoascii`, `pbmto4425`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmtoascii.html>.

- 1x2 픽셀 영역을 하나의 문자로 결합하여 PPM 이미지를 ASCII 이미지로 변환:

`ppmtoascii `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.txt</span>

- 2x4 픽셀 영역을 하나의 문자로 결합하여 PPM 이미지를 ASCII 이미지로 변환:

`ppmtoascii -2x4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.txt</span>
