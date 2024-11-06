---
layout: page
title: common/ppmtoxpm (한국어)
description: "PPM 이미지를 X11 버전 3 픽스맵으로 변환."
content_hash: afe7947700ffbcd0589dec9cc1ad095a27be6aea
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/ppmtoxpm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ppmtoxpm

PPM 이미지를 X11 버전 3 픽스맵으로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmtoxpm.html>.

- PPM 이미지를 XPM 이미지로 변환:

`ppmtoxpm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.xpm</span>

- 출력 XPM 이미지에서 접두사 문자열 지정:

`ppmtoxpm -name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">접두사_문자열</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.xpm</span>

- 출력 XPM 파일에서 색상을 이름 대신 16진수 코드로 지정:

`ppmtoxpm -hexonly `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.xpm</span>

- 지정된 PGM 파일을 투명 마스크로 사용:

`ppmtoxpm -alphamask `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/알파_파일.pgm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.xpm</span>
