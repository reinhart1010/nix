---
layout: page
title: common/supervisorctl (한국어)
description: "Supervisor는 UNIX 계열 운영 체제에서 여러 프로세스를 제어할 수 있게 해주는 클라이언트/서버 시스템입니다."
content_hash: 023f58bfacc5fb07dfff5edfaf001f7a55bdcf40
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/supervisorctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# supervisorctl

Supervisor는 UNIX 계열 운영 체제에서 여러 프로세스를 제어할 수 있게 해주는 클라이언트/서버 시스템입니다.
Supervisorctl은 shell과 유사한 인터페이스를 제공하는 supervisor의 명령줄 클라이언트입니다.
더 많은 정보: <http://supervisord.org>.

- 프로세스의 상태 표시 (`process_name`이 지정되지 않으면 모든 프로세스 표시):

`supervisorctl status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_이름</span>

- 프로세스 시작/중지/재시작:

`supervisorctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop|restart</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_이름</span>

- 그룹 내 모든 프로세스 시작/중지/재시작:

`supervisorctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop|restart</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_이름</span>`:*`

- 프로세스 `stderr`의 마지막 100바이트 표시:

`supervisorctl tail -100 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_이름</span>` stderr`

- 프로세스의 `stdout` 계속 표시:

`supervisorctl tail -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_이름</span>` stdout`

- 프로세스 구성 파일을 다시 로드하여 필요한 경우 프로세스를 추가/제거:

`supervisorctl update`
