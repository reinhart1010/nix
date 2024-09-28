---
layout: page
title: common/caddy (한국어)
description: "Go로 작성된 자동 HTTPS를 갖춘 엔터프라이즈급 오픈 소스 웹 서버."
content_hash: feb86baeacf29b673ef87dc60803438de4fde7a3
last_modified_at: 2024-09-28
related_topics:
  - title: Deutsch version
    url: /de/common/caddy.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/caddy.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/caddy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# caddy

Go로 작성된 자동 HTTPS를 갖춘 엔터프라이즈급 오픈 소스 웹 서버.
더 많은 정보: <https://caddyserver.com>.

- 포어그라운드에서 Caddy를 시작:

`caddy run`

- 지정된 Caddyfile로 Caddy를 시작:

`caddy run --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/Caddyfile</span>

- 백그라운드에서 Caddy를 시작:

`caddy start`

- 백그라운드 Caddy 프로세스를 중지:

`caddy stop`

- 탐색 가능한 인터페이스를 사용하여 지정된 포트에서 간단한 파일 서버를 실행:

`caddy file-server --listen :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8000</span>` --browse`

- 리버스 프록시 서버 실행:

`caddy reverse-proxy --from :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>` --to localhost:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8000</span>
