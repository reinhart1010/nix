---
layout: page
title: common/flips (한국어)
description: "IPS 및 BPS 파일용 패치를 생성하고 적용."
content_hash: 6f2475e4e8a37673a862a7f628d0ff87ad026567
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/flips.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/flips.html
    icon: bi bi-globe
tldri18n_status: 2
---
# flips

IPS 및 BPS 파일용 패치를 생성하고 적용.
더 많은 정보: <https://github.com/Alcaro/Flips>.

- 대화형으로 패치를 생성하고 적용하려면 Flips를 시작:

`flips`

- 패치를 적용하고 새 ROM 파일을 만듬:

`flips --apply `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patch.bps</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rom.smc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hack.smc</span>

- 두 개의 ROM에서 패치를 만듬:

`flips --create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rom.smc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hack.smc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patch.bps</span>
