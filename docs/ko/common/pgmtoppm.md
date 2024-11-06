---
layout: page
title: common/pgmtoppm (한국어)
description: "PGM 이미지를 색상화."
content_hash: ee4fed47805fa2f21ad39fb7e5c5d7b6ffa0daf7
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/pgmtoppm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pgmtoppm

PGM 이미지를 색상화.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pgmtoppm.html>.

- 입력 이미지의 모든 회색조 값을 두 가지 지정된 색상 사이의 모든 색상으로 매핑:

`pgmtoppm -black `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">red</span>` --white `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blue</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pgm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppm</span>

- 입력 이미지의 모든 회색조 값을 지정된 색상표에 따라 색상으로 매핑:

`pgmtoppm -map `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/색상표.ppm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pgm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppm</span>
