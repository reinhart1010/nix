---
layout: page
title: common/ps (한국어)
description: "실행 중인 프로세스에 대한 정보입니다."
content_hash: 84e5a08c06b83e88fc58a402b6a5432a4cb5712e
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/ps.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ps.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ps.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/ps.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ps

실행 중인 프로세스에 대한 정보입니다.
더 많은 정보: <https://manned.org/ps>.

- 실행 중인 모든 프로세스를 나열:

`ps aux`

- 전체 명령 문자열을 포함하여 실행 중인 모든 프로세스 나열:

`ps auxww`

- 문자열과 일치하는 프로세스 검색:

`ps aux | grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>

- 추가 전체 형식으로 현재 사용자의 모든 프로세스를 나열:

`ps --user $(id -u) -F`

- 현재 사용자의 모든 프로세스를 트리로 나열:

`ps --user $(id -u) f`

- 프로세스의 상위 PID 가져오기:

`ps -o ppid= -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- 메모리 소비를 기준으로 프로세스 정렬:

`ps --sort size`
