---
layout: page
title: common/pbmtonokia (한국어)
description: "PBM 이미지를 Nokia의 스마트 메시징 형식 중 하나로 변환."
content_hash: 828ba4e751f51d73384082b468846bc4afdf22d3
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/pbmtonokia.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pbmtonokia

PBM 이미지를 Nokia의 스마트 메시징 형식 중 하나로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pbmtonokia.html>.

- PBM 이미지를 Nokia 운영자 로고로 변환하여 헥스 코드로 출력:

`pbmtonokia -fmt NEX_NOL -net `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네트워크_운영자_코드</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.hex</span>

- PBM 이미지를 Nokia 그룹 그래픽으로 변환하여 헥스 코드로 출력:

`pbmtonokia -fmt NEX_NGG `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.hex</span>

- PBM 이미지를 지정된 텍스트와 함께 Nokia 그림 메시지로 변환하여 헥스 코드로 출력:

`pbmtonokia -fmt NEX_NPM -txt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">텍스트_메시지</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.hex</span>

- PBM 이미지를 Nokia 운영자 로고로 변환하여 NOL 파일로 출력:

`pbmtonokia -fmt NOL `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.nol</span>

- PBM 이미지를 Nokia 그룹 그래픽으로 변환하여 NGG 파일로 출력:

`pbmtonokia -fmt NGG `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ngg</span>

- PBM 이미지를 Nokia 그림 메시지로 변환하여 NPM 파일로 출력:

`pbmtonokia -fmt NPM `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.npm</span>
