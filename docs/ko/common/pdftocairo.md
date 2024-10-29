---
layout: page
title: common/pdftocairo (한국어)
description: "PDF 파일을 PNG/JPEG/TIFF/PDF/PS/EPS/SVG 형식으로 변환하는 도구입니다 (cairo 사용)."
content_hash: e8cde4a8ff43e2883459137cbce7af2ac1b3c692
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/common/pdftocairo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pdftocairo

PDF 파일을 PNG/JPEG/TIFF/PDF/PS/EPS/SVG 형식으로 변환하는 도구입니다 (cairo 사용).
더 많은 정보: <https://poppler.freedesktop.org>.

- PDF 파일을 JPEG로 변환:

`pdftocairo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>` -jpeg`

- 출력물이 용지를 채우도록 확장하여 PDF로 변환:

`pdftocairo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.pdf</span>` -pdf -expand`

- 변환할 첫 페이지와 마지막 페이지를 지정하여 SVG로 변환:

`pdftocairo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.svg</span>` -svg -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">첫_페이지</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">마지막_페이지</span>

- 200ppi 해상도로 PNG로 변환:

`pdftocairo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.png</span>` -png -r 200`

- A3 용지 크기로 설정하여 그레이스케일 TIFF로 변환:

`pdftocairo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>` -tiff -gray -paper A3`

- 좌측 상단 모서리에서 x와 y 픽셀을 잘라내어 PNG로 변환:

`pdftocairo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>` -png -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x_픽셀</span>` -y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y_픽셀</span>
