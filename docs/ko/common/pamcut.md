---
layout: page
title: common/pamcut (한국어)
description: "Netpbm 이미지에서 직사각형 영역을 잘라내기."
content_hash: 27204a30f97c2a517cfd941ce8d0fde92bed5f1a
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/pamcut.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pamcut.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pamcut

Netpbm 이미지에서 직사각형 영역을 잘라내기.
같이 보기: `pamcrop`, `pamdice`, `pamcomp`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pamcut.html>.

- 이미지의 양쪽에서 지정된 열/행 수만큼 잘라내기:

`pamcut -cropleft `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>` -cropright `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>` -croptop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>` -cropbottom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppm</span>

- 지정된 열 사이의 열만 유지하기 (포함):

`pamcut -left `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>` -right `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppm</span>

- 지정된 직사각형이 입력 이미지 내에 완전히 포함되지 않을 경우, 누락된 영역을 검은색 픽셀로 채우기:

`pamcut -top `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>` -bottom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>` -pad `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ppm</span>
