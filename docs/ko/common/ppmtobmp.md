---
layout: page
title: common/ppmtobmp (한국어)
description: "PPM 이미지를 BMP 파일로 변환."
content_hash: f105493e8c2755c31a169716827980f3490c8aca
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/ppmtobmp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ppmtobmp

PPM 이미지를 BMP 파일로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmtobmp.html>.

- PPM 이미지를 BMP 파일로 변환:

`ppmtobmp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.bmp</span>

- Windows BMP 파일 또는 OS/2 BMP 파일을 생성할지 여부를 명시적으로 지정:

`ppmtobmp -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">windows|os2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.bmp</span>

- 각 픽셀에 사용할 비트 수를 지정:

`ppmtobmp -bbp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|4|8|24</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.bmp</span>
