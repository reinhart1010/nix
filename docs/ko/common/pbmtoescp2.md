---
layout: page
title: common/pbmtoescp2 (한국어)
description: "PBM 이미지를 ESC/P2 프린터 파일로 변환."
content_hash: 806a42be8b647d25db591a104c6a7194b56ca6f2
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/pbmtoescp2.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pbmtoescp2

PBM 이미지를 ESC/P2 프린터 파일로 변환.
같이 보기: `pbmtoepson`, `escp2topbm`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pbmtoescp2.html>.

- PBM 이미지를 ESC/P2 프린터 파일로 변환:

`pbmtoescp2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.escp2</span>

- 출력의 압축 지정:

`pbmtoescp2 -compression `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.escp2</span>

- 출력을 인치당 도트 수로 가로 및 세로 해상도 지정:

`pbmtoescp2 -resolution `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">180|360|720</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.escp2</span>

- 출력의 끝에 폼피드 명령 추가:

`pbmtoescp2 -formfeed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.escp2</span>
