---
layout: page
title: common/pgmramp (한국어)
description: "그레이스케일 맵 생성."
content_hash: 9f4f8ef32d76c45ad04f1182b58f678051dca1a0
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/pgmramp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pgmramp

그레이스케일 맵 생성.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pgmramp.html>.

- 좌에서 우로 그레이스케일 맵 생성:

`pgmtexture -lr > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pgm</span>

- 위에서 아래로 그레이스케일 맵 생성:

`pgmtexture -tb > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pgm</span>

- 직사각형 그레이스케일 맵 생성:

`pgmtexture -rectangle > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pgm</span>

- 타원형 그레이스케일 맵 생성:

`pgmtexture -ellipse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pgm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pgm</span>

- 왼쪽 상단에서 오른쪽 하단으로 그레이스케일 맵 생성:

`pgmtexture -diagonal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pgm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pgm</span>
