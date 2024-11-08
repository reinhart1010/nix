---
layout: page
title: common/live-server (한국어)
description: "실시간 리로드 기능을 갖춘 간단한 개발 HTTP 서버."
content_hash: 4c054b4656465c1dd7bce7d7882615581c8ebe60
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/live-server.html
    icon: bi bi-globe
tldri18n_status: 2
---
# live-server

실시간 리로드 기능을 갖춘 간단한 개발 HTTP 서버.
더 많은 정보: <https://github.com/tapio/live-server>.

- `index.html` 파일을 제공하고 변경 시 리로드:

`live-server`

- 파일을 제공할 포트 지정 (기본값은 8080):

`live-server --port=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8081</span>

- 특정 파일을 제공:

`live-server --open=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">about.html</span>

- ROUTE에 대한 모든 요청을 URL로 프록시:

`live-server --proxy=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://localhost:3000</span>
