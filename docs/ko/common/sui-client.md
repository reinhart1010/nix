---
layout: page
title: common/sui-client (한국어)
description: "스마트 계약을 배포하고, 객체 정보를 얻고, 트랜잭션을 실행하는 등의 작업을 수행합니다."
content_hash: 48d3fae1ae03fb861c7ec1376f8dfaa22f0eaf2d
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/sui-client.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sui client

스마트 계약을 배포하고, 객체 정보를 얻고, 트랜잭션을 실행하는 등의 작업을 수행합니다.
더 많은 정보: <https://docs.sui.io/references/cli/client>.

- ED25519 스키마로 새 주소 생성:

`sui client new-address ed25519 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주소_별칭</span>

- RPC URL과 별칭으로 새 테스트넷 환경 생성:

`sui client new-env --rpc https://fullnode.testnet.sui.io:443 --alias testnet`

- 원하는 주소로 전환 (별칭도 허용):

`sui client switch --address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주소_별칭</span>

- 지정된 환경으로 전환:

`sui client switch --env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">환경_별칭</span>

- 스마트 계약 배포:

`sui client publish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_경로</span>

- Sui 파셋과 상호작용:

`sui client faucet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위명령어</span>

- 지정된 주소의 가스 코인 나열 (별칭도 허용):

`sui client gas `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주소</span>

- 프로그래머블 트랜잭션 블록 생성, 서명 및 실행:

`sui client ptb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">옵션</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위명령어</span>
