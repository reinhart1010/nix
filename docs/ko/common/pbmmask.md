---
layout: page
title: common/pbmmask (한국어)
description: "일반 비트맵에서 마스크 비트맵 생성."
content_hash: 7fc0ec3e178ba6282574d636c16a1301666c10ae
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/pbmmask.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pbmmask

일반 비트맵에서 마스크 비트맵 생성.
같이 보기: `pambackground`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pbmmask.html>.

- 배경과 전경을 분리하여 마스크 비트맵 생성:

`pbmmask `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pbm</span>

- 생성된 마스크를 한 픽셀 확장:

`pbmmask -expand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pbm</span>
