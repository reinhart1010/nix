---
layout: page
title: common/bitcoind (한국어)
description: "Bitcoin Core 데몬."
content_hash: 1f4470cc768d7c0e9584e210516e76107e57361d
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/common/bitcoind.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/bitcoind.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bitcoind

Bitcoin Core 데몬.
`bitcoin.conf`에 정의된 구성을 사용.
더 많은 정보: <https://manned.org/bitcoind>.

- 비트코인 코어 데몬을 시작 (포어그라운드 환경에서):

`bitcoind`

- 백그라운드에서 Bitcoin Core 데몬을 시작 (중지하려면 `bitcoin-cli stop` 사용):

`bitcoind -daemon`

- 특정 네트워크에서 Bitcoin Core 데몬을 시작:

`bitcoind -chain=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">main|test|signet|regtest</span>

- 특정 구성 파일 및 데이터 디렉터리를 사용하여 Bitcoin Core 데몬을 시작:

`bitcoind -conf=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/bitcoin.conf</span>` -datadir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>
