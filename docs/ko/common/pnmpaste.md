---
layout: page
title: common/pnmpaste (한국어)
description: "PNM 이미지를 다른 PNM 이미지에 붙여 넣기."
content_hash: 209124cc19ff4bc84eda2a5d6dc972f149ba91a5
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/pnmpaste.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pnmpaste

PNM 이미지를 다른 PNM 이미지에 붙여 넣기.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pnmpaste.html>.

- 지정된 좌표에 PNM 이미지를 다른 PNM 이미지에 붙여 넣기:

`pnmpaste `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지1.pnm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지2.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>

- `stdin`에서 읽은 이미지를 지정된 이미지에 붙여 넣기:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | pnmpaste `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>

- 겹치는 픽셀을 지정된 불리언 연산으로 결합하기, 이때 흰색 픽셀은 `true`, 검은색 픽셀은 `false`로 표현:

`pnmpaste -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">and|nand|or|nor|xor|xnor</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지1.pnm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지2.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pnm</span>
