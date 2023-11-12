---
layout: page
title: common/bitcoin-cli (한국어)
description: "RPC 호출을 통해 비트코인 데몬과 상호 작용하는 커맨드라인 클라이언트.`bitcoin.conf`에 정의된 구성 사용."
content_hash: 40f42e09141e1f28d3a782919f564a423e437872
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/bitcoin-cli.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bitcoin-cli.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/bitcoin-cli.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bitcoin-cli

RPC 호출을 통해 비트코인 데몬과 상호 작용하는 커맨드라인 클라이언트.`bitcoin.conf`에 정의된 구성 사용.
더 많은 정보: <https://en.bitcoin.it/wiki/Running_Bitcoin#Command-line_arguments>.

- 지정된 주소로 트랜잭션 전송:

`bitcoin-cli sendtoaddress "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주소</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">양</span>

- 하나 이상의 블록 생성:

`bitcoin-cli generate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">블록_갯수</span>

- wallet에 대한 고급 정보 출력:

`bitcoin-cli getwalletinfo`

- 보내지지 않은 모든 트랜잭션의 출력 나열:

`bitcoin-cli listunspent`

- wallet 정보를 텍스트 파일로 출력:

`bitcoin-cli dumpwallet "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일/의/경로</span>`"`
