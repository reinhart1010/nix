---
layout: page
title: linux/pihole (한국어)
description: "Pi-hole 광고 차단 DNS 서버의 터미널 인터페이스."
content_hash: 6f58def93b603c1b77033b01a3ed8a5515179cda
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/pihole.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/pihole.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pihole

Pi-hole 광고 차단 DNS 서버의 터미널 인터페이스.
더 많은 정보: <https://docs.pi-hole.net/core/pihole-command/>.

- Pi-hole 데몬의 상태 확인:

`pihole status`

- Pi-hole 및 Gravity 업데이트:

`pihole -up`

- 시스템 상태 자세히 모니터링:

`pihole chronometer`

- 데몬 시작 또는 중지:

`pihole `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enable|disable</span>

- 데몬 재시작 (서버 자체는 아님):

`pihole restartdns`

- 도메인 화이트리스트 또는 블랙리스트에 추가:

`pihole `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">whitelist|blacklist</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 도메인을 목록에서 검색:

`pihole query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 연결의 실시간 로그 열기:

`pihole tail`
