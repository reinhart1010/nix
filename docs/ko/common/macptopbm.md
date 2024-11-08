---
layout: page
title: common/macptopbm (한국어)
description: "MacPaint 파일을 입력으로 받아 PBM 이미지를 출력으로 생성합니다."
content_hash: 663b031b405241dbf7767dac34515022051ce9bc
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/macptopbm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# macptopbm

MacPaint 파일을 입력으로 받아 PBM 이미지를 출력으로 생성합니다.
같이 보기: `pbmtomacp`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/macptopbm.html>.

- MacPaint 파일을 PGM 이미지로 변환:

`macptopbm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.macp</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pbm</span>

- 파일을 읽을 때 지정된 바이트 수만큼 건너뜀:

`macptopbm -extraskip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pbm</span>

- 모든 정보 메시지 억제:

`macptopbm -quiet > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pbm</span>

- 버전 표시:

`macptopbm -version`
