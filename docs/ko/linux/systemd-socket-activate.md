---
layout: page
title: linux/systemd-socket-activate (한국어)
description: "systemd 서비스의 소켓 활성화."
content_hash: 8310c6a4e15b2800716b6270c07ecd0245b7ec7a
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/linux/systemd-socket-activate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# systemd-socket-activate

systemd 서비스의 소켓 활성화.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemd-socket-activate.html>.

- 특정 소켓이 연결되었을 때 서비스를 활성화:

`systemd-socket-activate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/socket.service</span>

- 서비스에 대해 여러 소켓을 활성화:

`systemd-socket-activate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/socket1.service</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/socket2.service</span>

- 활성화되는 서비스에 환경 변수를 전달:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SYSTEMD_SOCKET_ACTIVATION=1</span>` systemd-socket-activate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/socket.service</span>

- 알림 소켓과 함께 서비스를 활성화:

`systemd-socket-activate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/socket.socket</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/service.service</span>

- 지정된 포트로 서비스를 활성화:

`systemd-socket-activate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/socket.service</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8080</span>
