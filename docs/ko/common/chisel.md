---
layout: page
title: common/chisel (한국어)
description: "TCP/UDP 터널 생성, HTTP를 통해 전송, SSH를 통해 보안."
content_hash: 200d86e08fbf1de18fc95f33b1574c9b7d5bd336
last_modified_at: 2024-11-26
related_topics:
  - title: English version
    url: /en/common/chisel.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># chisel

TCP/UDP 터널 생성, HTTP를 통해 전송, SSH를 통해 보안.
동일한 `chisel` 실행 파일에 클라이언트와 서버 모두 포함됩니다.
더 많은 정보: <https://github.com/jpillora/chisel>.

- Chisel 서버 실행:

`chisel server`

- 특정 포트를 수신하는 Chisel 서버 실행:

`chisel server -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버_포트</span>

- 사용자 이름 및 암호 인증을 사용하여 연결을 보호하는 Chisel 서버 실행:

`chisel server --auth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>

- Chisel 서버에 연결하고 특정 포트를 원격 서버 와 포트에 터널링:

`chisel client `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버_IP</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버_포트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">로컬_포트</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_서버</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_포트</span>

- Chisel 서버에 연결하고 특정 호스트와 포트를 원격 서버 및 포트에 터널링:

`chisel client `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버_IP</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버_포트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">로컬_호스트</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">로컬_포트</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_서버</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_포트</span>

- 사용자 이름 및 암호 인증을 사용하여 Chisel 서버에 연결:

`chisel client --auth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버_IP</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버_포트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">로컬_포트</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_서버</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_포트</span>

- 특정 포트에서 역방향 모드로 Chisel 서버 초기화, 또한 SOCKS5 프록시(포트 1080) 기능 활성화:

`chisel server -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버_포트</span>` --reverse --socks5`

- 특정 IP 및 포트에서 Chisel 서버에 연결하고 로컬 SOCKS 프록시에 매핑된 역방향 터널 생성:

`chisel client `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버_IP</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버_포트</span>` R:socks`
