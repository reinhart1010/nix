---
layout: page
title: common/var-dump-server (한국어)
description: "Symfony 덤프 서버."
content_hash: f7c5f74bd71cd24ff47be0409445bce9d5c46a4a
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/common/var-dump-server.html
    icon: bi bi-globe
tldri18n_status: 2
---
# var-dump-server

Symfony 덤프 서버.
Symfony VarDumper 컴포넌트에 의해 덤프된 데이터를 수집합니다.
더 많은 정보: <https://symfony.com/doc/current/components/var_dumper.html#the-dump-server>.

- 서버 시작:

`var-dump-server`

- 데이터를 HTML 파일로 덤프:

`var-dump-server --format=html > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.html</span>

- 특정 주소와 포트에서 서버 수신 대기:

`var-dump-server --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">127.0.0.1:9912</span>
