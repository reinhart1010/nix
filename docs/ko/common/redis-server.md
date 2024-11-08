---
layout: page
title: common/redis-server (한국어)
description: "영구적인 키-값 데이터베이스."
content_hash: 45c4f48f5a11cfd9cfa3df6474827baccc6e635e
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/redis-server.html
    icon: bi bi-globe
tldri18n_status: 2
---
# redis-server

영구적인 키-값 데이터베이스.
더 많은 정보: <https://redis.io>.

- 기본 포트(6379)를 사용하여 Redis 서버 시작 및 로그를 `stdout`으로 출력:

`redis-server`

- 기본 포트를 사용하여 백그라운드 프로세스로 Redis 서버 시작:

`redis-server --daemonize yes`

- 지정된 포트를 사용하여 백그라운드 프로세스로 Redis 서버 시작:

`redis-server --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>` --daemonize yes`

- 사용자 지정 구성 파일을 사용하여 Redis 서버 시작:

`redis-server `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/redis.conf</span>

- 상세 로그를 출력하며 Redis 서버 시작:

`redis-server --loglevel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">warning|notice|verbose|debug</span>
