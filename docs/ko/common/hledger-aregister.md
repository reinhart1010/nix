---
layout: page
title: common/hledger-aregister (한국어)
description: "한 계좌의 거래 내역과 잔액을 한 줄로 표시."
content_hash: de7986c60dbee543e7460200fdd3d5ac8fc65853
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/hledger-aregister.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hledger aregister

한 계좌의 거래 내역과 잔액을 한 줄로 표시.
더 많은 정보: <https://hledger.org/hledger.html#aregister>.

- `assets:bank:checking` 계좌의 거래 내역과 잔액 표시:

`hledger aregister assets:bank:checking`

- `*savings*`라는 이름의 첫 번째 계좌의 거래 내역과 잔액 표시:

`hledger aregister savings`

- 지정된 너비로 체크 계좌의 정리된 거래 내역 표시:

`hledger aregister checking --cleared --width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">120</span>

- 예측 규칙의 거래를 포함하여 체크 계좌의 내역 표시:

`hledger aregister checking --forecast`
