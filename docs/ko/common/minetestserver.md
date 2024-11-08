---
layout: page
title: common/minetestserver (한국어)
description: "멀티플레이어 무한 세계 블록 샌드박스 서버."
content_hash: a42ed6c3604517afb0f567c2e4f2881b3a4fafb2
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/minetestserver.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/minetestserver.html
    icon: bi bi-globe
tldri18n_status: 2
---
# minetestserver

멀티플레이어 무한 세계 블록 샌드박스 서버.
그래픽 클라이언트인 `minetest`도 참고하세요.
더 많은 정보: <https://wiki.minetest.org/Setting_up_a_server>.

- 서버 시작:

`minetestserver`

- 사용 가능한 세계 목록 나열:

`minetestserver --world list`

- 지정된 세계 로드:

`minetestserver --world `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">세계_이름</span>

- 사용 가능한 게임 ID 목록 나열:

`minetestserver --gameid list`

- 지정된 게임 사용:

`minetestserver --gameid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">게임_ID</span>

- 특정 포트로 수신 대기:

`minetestserver --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">34567</span>

- 다른 데이터 백엔드로 마이그레이션:

`minetestserver --migrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sqlite3|leveldb|redis</span>

- 서버 시작 후 대화형 터미널 시작:

`minetestserver --terminal`
