---
layout: page
title: common/pbmtoascii (한국어)
description: "PBM 이미지를 ASCII 그래픽으로 변환."
content_hash: c043e209c0d16fde2d756e796a5c60b971af8774
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/pbmtoascii.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pbmtoascii

PBM 이미지를 ASCII 그래픽으로 변환.
같이 보기: `ppmtoascii`, `asciitopgm`, `ppmtoterm`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pbmtoascii.html>.

- PBM 파일을 입력으로 받고 ASCII 출력 생성:

`pbmtoascii `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.pbm</span>

- PBM 파일을 입력으로 받고 ASCII 출력을 파일로 저장:

`pbmtoascii `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>

- 픽셀 매핑을 설정하여 PBM 파일을 입력으로 받기 (기본값은 1x2):

`pbmtoascii -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1x2|2x4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일.pbm</span>

- 버전 표시:

`pbmtoascii -version`
