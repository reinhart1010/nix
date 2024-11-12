---
layout: page
title: linux/sslstrip (한국어)
description: "Moxie Marlinspike의 Secure Sockets Layer (SSL) 스트리핑 공격을 수행합니다."
content_hash: f365e79b057e4ecbdb3ba8732155fc83d2256bf1
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/sslstrip.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/sslstrip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sslstrip

Moxie Marlinspike의 Secure Sockets Layer (SSL) 스트리핑 공격을 수행합니다.
ARP 스푸핑 공격을 함께 수행합니다.
더 많은 정보: <https://www.kali.org/tools/sslstrip/>.

- 기본으로 포트 10000에서 HTTPS POST 트래픽만 로깅:

`sslstrip`

- 포트 8080에서 HTTPS POST 트래픽만 로깅:

`sslstrip --listen=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8080</span>

- 포트 8080에서 서버와 주고받는 모든 SSL 트래픽 로깅:

`sslstrip --ssl --listen=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8080</span>

- 포트 8080에서 서버와 주고받는 모든 SSL 및 HTTP 트래픽 로깅:

`sslstrip --listen=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8080</span>` --all`

- 로그를 저장할 파일 경로 지정:

`sslstrip --listen=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8080</span>` --write=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 도움말 표시:

`sslstrip --help`
