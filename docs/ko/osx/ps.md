---
layout: page
title: osx/ps (한국어)
description: "실행 중인 프로세스에 대한 정보."
content_hash: df8ac4a392ba2f6e679e8cc85c8fd523031a86bf
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/ps.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/ps.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/ps.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ps

실행 중인 프로세스에 대한 정보.
더 많은 정보: <https://keith.github.io/xcode-man-pages/ps.1.html>.

- 모든 실행 중인 프로세스 나열:

`ps aux`

- 전체 명령어 문자열을 포함하여 모든 실행 중인 프로세스 나열:

`ps auxww`

- 문자열과 일치하는 프로세스 검색:

`ps aux | grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>

- 프로세스의 부모 PID 가져오기:

`ps -o ppid= -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- 메모리 사용량으로 프로세스 정렬:

`ps -m`

- CPU 사용량으로 프로세스 정렬:

`ps -r`
