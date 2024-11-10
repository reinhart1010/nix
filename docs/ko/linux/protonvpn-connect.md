---
layout: page
title: linux/protonvpn-connect (한국어)
description: "ProtonVPN에 연결."
content_hash: 231b09bf4c203e9d30bb49b9b3e6cd1770436d50
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/protonvpn-connect.html
    icon: bi bi-globe
tldri18n_status: 2
---
# protonvpn connect

ProtonVPN에 연결.
더 많은 정보: <https://github.com/Rafficer/linux-cli-community>.

- ProtonVPN에 대화식으로 연결:

`protonvpn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">c|connect</span>

- 사용 가능한 가장 빠른 서버로 ProtonVPN에 연결:

`protonvpn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">c|connect</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--fastest</span>

- 특정 서버와 특정 프로토콜로 ProtonVPN에 연결:

`protonvpn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">c|connect</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버_이름</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">udp|tcp</span>

- 임의의 서버와 특정 프로토콜로 ProtonVPN에 연결:

`protonvpn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">c|connect</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--random</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">udp|tcp</span>

- Tor를 지원하는 가장 빠른 서버로 ProtonVPN에 연결:

`protonvpn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">c|connect</span>` --tor`

- 도움말 표시:

`protonvpn connect --help`
