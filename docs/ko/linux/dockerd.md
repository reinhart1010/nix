---
layout: page
title: linux/dockerd (한국어)
description: "Docker 컨테이너를 시작하고 관리하는 지속적인 프로세스."
content_hash: f3e3e1171a10b52f72a1fa0f3b3a26d0590fd090
last_modified_at: 2024-11-09
related_topics:
  - title: العربية version
    url: /ar/linux/dockerd.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dockerd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dockerd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dockerd

Docker 컨테이너를 시작하고 관리하는 지속적인 프로세스.
더 많은 정보: <https://docs.docker.com/reference/cli/dockerd/>.

- Docker 데몬 실행:

`dockerd`

- Docker 데몬을 실행하고 특정 소켓(UNIX 및 TCP)을 수신하도록 설정:

`dockerd --host unix://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/tmp.sock</span>` --host tcp://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP</span>

- 특정 데몬 PID 파일로 실행:

`dockerd --pidfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/PID_파일</span>

- 디버그 모드로 실행:

`dockerd --debug`

- 특정 로그 레벨로 실행:

`dockerd --log-level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">debug|info|warn|error|fatal</span>
