---
layout: page
title: common/pbmtoppa (한국어)
description: "PBM 이미지를 HP 프린터 성능 아키텍처 형식으로 변환."
content_hash: f170025f28caf17f0e2030684bf458b79636d749
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/pbmtoppa.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pbmtoppa

PBM 이미지를 HP 프린터 성능 아키텍처 형식으로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pbmtoppa.html>.

- PBM 이미지를 PPA 파일로 변환:

`pbmtoppa `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppa</span>

- 원하는 인치당 도트 수와 용지 크기 지정:

`pbmtoppa -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">300</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppa</span>
