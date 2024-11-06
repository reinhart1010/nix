---
layout: page
title: common/ppmntsc (한국어)
description: "PPM 이미지의 RGB 색상을 NTSC 또는 PAL 컬러 시스템과 호환되도록 만듭니다."
content_hash: 4dba11281dea715ceb9fd436fc72278a6fe0ea10
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/ppmntsc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ppmntsc

PPM 이미지의 RGB 색상을 NTSC 또는 PAL 컬러 시스템과 호환되도록 만듭니다.
더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmntsc.html>.

- PPM 이미지의 RGB 색상을 NTSC 컬러 시스템과 호환되도록 만들기:

`ppmntsc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.ppm</span>

- PPM 이미지의 RGB 색상을 PAL 컬러 시스템과 호환되도록 만들기:

`ppmntsc --pal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.ppm</span>

- 입력 이미지의 불법 픽셀 수를 `stderr`에 출력:

`ppmntsc --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.ppm</span>

- 합법/불법/수정된 픽셀만 출력하고 다른 픽셀은 검정색으로 설정:

`ppmntsc --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">legalonly|illegalonly|correctedonly</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.ppm</span>
