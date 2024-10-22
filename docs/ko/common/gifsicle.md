---
layout: page
title: common/gifsicle (한국어)
description: "GIF 파일에 대한 정보를 생성, 편집, 조작 및 가져옴."
content_hash: 19a2c4ba6019589ff83cf7cc3f7727a7b237e910
last_modified_at: 2024-10-22
related_topics:
  - title: English version
    url: /en/common/gifsicle.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gifsicle

GIF 파일에 대한 정보를 생성, 편집, 조작 및 가져옴.
더 많은 정보: <https://www.lcdf.org/gifsicle>.

- GIF를 새로운 파일로 최적화:

`gifsicle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력파일.gif</span>` --optimize=3 -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력파일.gif</span>

- [b]atch 모드를 사용하고 (주어진 각 파일을 제자리에서 수정) GIF 최적화를 취소:

`gifsicle -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력파일.gif</span>` --unoptimize`

- GIF에서 프레임 추출:

`gifsicle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력파일.gif</span>` '#`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>`' > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/첫번째_프레임.gif</span>

- 선택한 GIF로 GIF 애니메이션 만들기:

`gifsicle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.gif</span>` --delay=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` --loop > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력파일.gif</span>

- 손실 압축을 사용하여 파일 크기 줄이기 :

`gifsicle -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력파일.gif</span>` --optimize=3 --lossy=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --colors=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">16</span>` --dither`

- GIF에서 처음 10개 프레임과 20개 이후 프레임 모두를 삭제:

`gifsicle -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력파일.gif</span>` --delete '#`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0-9</span>`' '#`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20-</span>`'`

- 직사각형으로 자르고, 비율을 변경하고, 뒤집고, 회전하여 모든 프레임을 수정:

`gifsicle -b --crop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x시작점</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y시작점</span>`+`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">직사각형_너비</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">직사각형_높이</span>` --scale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.25</span>` --flip-horizontal --rotate-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">90|180|270</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력파일.gif</span>
