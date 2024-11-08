---
layout: page
title: common/picttoppm (한국어)
description: "Macintosh PICT 파일을 PPM 이미지로 변환."
content_hash: b5173ba1d6c00f482d7679841310ea17c3c9d84a
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/picttoppm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# picttoppm

Macintosh PICT 파일을 PPM 이미지로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/picttoppm.html>.

- PICT 파일을 PPM 이미지로 변환:

`picttoppm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pict</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>

- PICT 파일의 모든 이미지를 최대 해상도로 출력하도록 강제:

`picttoppm -fullres `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pict</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>

- 입력 파일에 PICT 헤더가 포함되어 있다고 가정하지 않고, quickdraw 작업만 실행:

`picttoppm -noheader -quickdraw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pict</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>
