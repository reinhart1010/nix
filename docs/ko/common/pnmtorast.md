---
layout: page
title: common/pnmtorast (한국어)
description: "PNM 파일을 Sun 래스터 파일로 변환."
content_hash: 920fcc8e1b9fb202bdd3b53df6970293def8a447
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/pnmtorast.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pnmtorast

PNM 파일을 Sun 래스터 파일로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmtorast.html>.

- PNM 이미지를 RAST 이미지로 변환:

`pnmtorast `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.rast</span>

- 출력 형식을 `RT_STANDARD` 또는 `RT_BYTE_ENCODED` 형식으로 강제 지정:

`pnmtorast -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">standard|rle</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.rast</span>
