---
layout: page
title: common/supervisord (한국어)
description: "Supervisor는 유닉스 계열 운영 체제에서 일부 프로세스를 제어하기 위한 클라이언트/서버 시스템입니다."
content_hash: 79297b2f62909fbf85b6dac0e2a8e86c81ec3a26
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/supervisord.html
    icon: bi bi-globe
tldri18n_status: 2
---
# supervisord

Supervisor는 유닉스 계열 운영 체제에서 일부 프로세스를 제어하기 위한 클라이언트/서버 시스템입니다.
Supervisord는 Supervisor의 서버 부분으로, 주로 구성 파일을 통해 관리됩니다.
더 많은 정보: <http://supervisord.org>.

- 지정된 구성 파일로 `supervisord` 시작:

`supervisord -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 포그라운드에서 supervisord 실행:

`supervisord -n`
