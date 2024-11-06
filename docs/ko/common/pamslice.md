---
layout: page
title: common/pamslice (한국어)
description: "PAM 이미지에서 한 줄의 값을 추출."
content_hash: 8d3f7a11fb6b6cca0279c48eaee3f38b605e12f3
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/pamslice.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/pamslice.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pamslice.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pamslice

PAM 이미지에서 한 줄의 값을 추출.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pamslice.html>.

- n번째 행의 픽셀 값을 테이블 형식으로 출력:

`pamslice -row `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pam</span>

- n번째 열의 픽셀 값을 테이블 형식으로 출력:

`pamslice -column `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pam</span>

- 입력 이미지의 m번째 평면만 고려:

`pamslice -row `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` -plane `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">m</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pam</span>

- 시각화를 위한 `xmgr` 입력 형식으로 출력 생성:

`pamslice -row `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` -xmgr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pam</span>
