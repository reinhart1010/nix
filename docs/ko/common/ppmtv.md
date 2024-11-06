---
layout: page
title: common/ppmtv (한국어)
description: "PPM 이미지를 미국 TV에서 찍은 것처럼 보이게 만듭니다."
content_hash: bbd28c3a52d2f9464a5703384b503e9e0bbae601
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/ppmtv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ppmtv

PPM 이미지를 미국 TV에서 찍은 것처럼 보이게 만듭니다.
이미지 데이터의 모든 다른 행을 지정된 감쇠 계수(0과 1 사이의 숫자)로 줄입니다.
더 많은 정보: <https://netpbm.sourceforge.net/doc/ppmtv.html>.

- PPM 이미지에 미국 TV 효과 적용:

`ppmtv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">감쇠_계수</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppm</span>

- 모든 정보 메시지 억제:

`ppmtv -quiet`

- 버전 표시:

`ppmtv -version`
