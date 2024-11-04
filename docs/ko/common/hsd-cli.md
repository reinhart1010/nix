---
layout: page
title: common/hsd-cli (한국어)
description: "Handshake 블록체인용 커멘드 라인 REST 도구."
content_hash: 633c31ae33afe7d511ff181b331703d730d10798
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/common/hsd-cli.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hsd-cli

Handshake 블록체인용 커멘드 라인 REST 도구.
더 많은 정보: <https://handshake.org>.

- 현재 서버에 대한 정보 검색:

`hsd-cli info`

- 로컬 트랜잭션 브로드캐스트:

`hsd-cli broadcast `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">트랜잭션_16진수값</span>

- mempool 스냅샷 검색:

`hsd-cli mempool`

- 주소 또는 해시로 트랜잭션 보기:

`hsd-cli tx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주소_또는_해시</span>

- 해시 인덱스 또는 주소로 코인 보기:

`hsd-cli coin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">해시_인덱스_또는_주소</span>

- 높이 또는 해시별로 블록 보기:

`hsd-cli block `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">높이_또는_해시</span>

- 지정된 블록으로 체인을 재설정:

`hsd-cli reset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">높이_또는_해시</span>

- RPC 명령을 실행:

`hsd-cli rpc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인자</span>
