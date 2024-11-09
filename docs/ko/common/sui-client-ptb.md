---
layout: page
title: common/sui-client-ptb (한국어)
description: "프로그래머블 트랜잭션 블록 생성, 서명 및 실행."
content_hash: a7d627b79d2879048b1c77a79377181ffb476e2a
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/sui-client-ptb.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sui-client-ptb.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sui client ptb

프로그래머블 트랜잭션 블록 생성, 서명 및 실행.
더 많은 정보: <https://docs.sui.io/references/cli/ptb>.

- 패키지와 모듈에서 Move 함수 호출:

`sui client ptb --move-call p::m::f "<`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">타입</span>`>" args`

- u64 타입의 두 요소로 Move 벡터 생성:

`sui client ptb --make-move-vec "<u64>" "[1000,2000]"`

- 가스 코인을 분할하고 주소로 전송:

`sui client ptb --split-coins gas "[1000]" --assign new_coins --transfer-objects "[new_coins]" @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주소</span>

- 객체를 주소로 전송:

`sui client ptb --transfer-objects "[`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">객체_ID</span>`]" @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주소</span>

- Move 패키지를 게시하고 업그레이드 기능을 송신자에게 전송:

`sui client ptb --move-call sui::tx_context::sender --assign sender --publish "." --assign upgrade_cap --transfer-objects "[upgrade_cap]" sender`
