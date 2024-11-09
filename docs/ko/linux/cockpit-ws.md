---
layout: page
title: linux/cockpit-ws (한국어)
description: "브라우저 애플리케이션과 `cockpit-bridge`와 같은 다양한 구성 도구 및 서비스 간 통신."
content_hash: e9dc3c3580dfc05310bea7607a6ecc5d70daee92
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/cockpit-ws.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cockpit-ws

브라우저 애플리케이션과 `cockpit-bridge`와 같은 다양한 구성 도구 및 서비스 간 통신.
더 많은 정보: <https://cockpit-project.org/guide/latest/cockpit-ws.8.html>.

- `127.0.0.1`에서 포트 `22`로 SSH 인증을 통해 시작:

`cockpit-ws --local-ssh`

- 특정 포트에서 HTTP 서버 시작:

`cockpit-ws --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 특정 IP 주소에 바인딩하여 시작 (기본값은 `0.0.0.0`):

`cockpit-ws --address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_주소</span>

- TLS 없이 시작:

`cockpit-ws --no-tls`

- 도움말 표시:

`cockpit-ws --help`
