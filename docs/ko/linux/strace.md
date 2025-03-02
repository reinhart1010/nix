---
layout: page
title: linux/strace (한국어)
description: "시스템 호출을 추적하는 문제 해결 도구."
content_hash: d50838ef4ec93faf6f89cbfc6c22a8840c5b72a1
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/strace.html
    icon: bi bi-globe
tldri18n_status: 2
---
# strace

시스템 호출을 추적하는 문제 해결 도구.
더 많은 정보: <https://manned.org/strace>.

- 특정 [p]프로세스를 PID로 추적 시작:

`strace -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- [p]프로세스를 추적하고 시스템 호출로 출력을 필터링:

`strace -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system_call,system_call2,...</span>

- 각 시스템 호출에 대해 시간, 호출 횟수, 오류 수를 계산하고 프로그램 종료 시 요약 보고:

`strace -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>` -c`

- 각 시스템 호출에 소요된 [T]시간을 표시하고 출력할 문자열 최대 크기 지정:

`strace -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>` -T -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">32</span>

- 프로그램을 실행하여 추적 시작:

`strace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로그램</span>

- 파일 작업을 추적 시작:

`strace -e trace=file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로그램</span>

- 프로그램의 네트워크 작업과 모든 [f]포크된 및 자식 프로세스를 추적하고 [o]출력을 파일에 저장:

`strace -f -e trace=network -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">추적.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로그램</span>
