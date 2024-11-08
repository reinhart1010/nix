---
layout: page
title: common/pstopnm (한국어)
description: "PostScript 파일을 PNM 이미지로 변환."
content_hash: dba9237818be6e209987a247d7fd86b3d47bcfa9
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/pstopnm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pstopnm

PostScript 파일을 PNM 이미지로 변환.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pstopnm.html>.

- PS 파일을 PNM 이미지로 변환하고 입력의 페이지 N을 `path/to/fileN.ppm`에 저장:

`pstopnm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ps</span>

- 출력 형식 명시적으로 지정:

`pstopnm -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pbm|pgm|ppm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ps</span>

- 출력 해상도를 인치당 도트로 지정:

`pstopnm -dpi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ps</span>
