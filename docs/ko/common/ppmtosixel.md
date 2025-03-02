---
layout: page
title: common/ppmtosixel (한국어)
description: "PPM 이미지를 DEC sixel 형식으로 변환."
content_hash: 1e8a648050b20b610bc12d15c83e86e11276d48b
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/ppmtosixel.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ppmtosixel

PPM 이미지를 DEC sixel 형식으로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmtosixel.html>.

- PPM 이미지를 DEC sixel 형식으로 변환:

`ppmtosixel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.sixel</span>

- 인쇄 속도가 훨씬 느린 비압축 SIXEL 파일 생성:

`ppmtosixel -raw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.sixel</span>

- 왼쪽 여백을 1.5인치 추가:

`ppmtosixel -margin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.sixel</span>

- 제어 코드를 보다 이식 가능하게(공간 효율성은 떨어짐) 인코딩:

`ppmtosixel -7bit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.sixel</span>
