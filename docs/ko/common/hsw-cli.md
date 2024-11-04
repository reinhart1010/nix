---
layout: page
title: common/hsw-cli (한국어)
description: "Handshake 지갑을 위한 커멘드 라인 REST 도구."
content_hash: 59715f47f28613d0c2d17de5783c95859c1b677d
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/common/hsw-cli.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hsw-cli

Handshake 지갑을 위한 커멘드 라인 REST 도구.
더 많은 정보: <https://github.com/handshake-org/hs-client>.

- 현재 지갑 잠금 해제 (초 단위 시간 초과):

`hsw-cli unlock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">암호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시간</span>

- 현재 지갑을 잠금:

`hsw-cli lock`

- 현재 지갑의 세부정보 보기:

`hsw-cli get`

- 현재 지갑 잔액 보기:

`hsw-cli balance`

- 현재 지갑의 거래 내역 보기:

`hsw-cli history`

- 지정된 코인 금액으로 트랜잭션을 주소로 보냄:

`hsw-cli send `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주소</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.05</span>

- 현재 지갑의 보류 중인 트랜잭션을 확인:

`hsw-cli pending`

- 트랜잭션 세부정보 보기:

`hsw-cli tx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">트랜잭션_해시</span>
