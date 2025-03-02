---
layout: page
title: linux/cockpit-tls (한국어)
description: "클라이언트와 `cockpit-ws` 간의 트래픽을 암호화하기 위한 TLS 종료 HTTP 프록시."
content_hash: ca77a0ceaada437c7fcb5ec6b8178f79c5efb92c
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/cockpit-tls.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cockpit-tls

클라이언트와 `cockpit-ws` 간의 트래픽을 암호화하기 위한 TLS 종료 HTTP 프록시.
더 많은 정보: <https://cockpit-project.org/guide/latest/cockpit-tls.8.html>.

- 특정 포트로 HTTP 요청을 제공 (기본 포트 `9090` 대신):

`cockpit-tls --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 도움말 표시:

`cockpit-tls --help`
