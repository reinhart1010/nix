---
layout: page
title: common/pamtogif (한국어)
description: "Netpbm 이미지를 애니메이션이 없는 GIF 이미지로 변환."
content_hash: d84bf1a01f46dd4c40291cb836dfa846f456d96f
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/pamtogif.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/pamtogif.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pamtogif.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pamtogif

Netpbm 이미지를 애니메이션이 없는 GIF 이미지로 변환.
같이 보기: `giftopnm`, `gifsicle`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pamtogif.html>.

- Netpbm 이미지를 애니메이션이 없는 GIF 이미지로 변환:

`pamtogif `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.gif</span>

- 출력 GIF 파일에서 지정한 색상을 투명하게 설정:

`pamtogif -transparent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">색상</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.gif</span>

- 출력 GIF 파일에 지정한 텍스트를 주석으로 포함:

`pamtogif -comment "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World!</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.gif</span>
