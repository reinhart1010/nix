---
layout: page
title: common/doctl-balance (한국어)
description: "Digital Ocean 계정의 잔액을 표시."
content_hash: 327b55f857873adff40acead1852363eb2e89b81
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/doctl-balance.html
    icon: bi bi-globe
tldri18n_status: 2
---
# doctl balance

Digital Ocean 계정의 잔액을 표시.
더 많은 정보: <https://docs.digitalocean.com/reference/doctl/reference/balance/>.

- 현재 컨텍스트와 관련된 계정의 잔액을 가져옴:

`doctl balance get`

- 액세스 토큰과 연결된 계정 잔액을 가져옴:

`doctl balance get --access-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">액세스_토큰</span>

- 지정된 컨텍스트와 연결된 계정의 잔액을 가져옴:

`doctl balance get --context`
