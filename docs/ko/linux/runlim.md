---
layout: page
title: linux/runlim (한국어)
description: "Linux의 proc 파일 시스템을 사용하여 프로그램 및 자식 프로세스의 시간 및 메모리 사용량을 샘플링하고 제한합니다."
content_hash: 0607a3f35d18e50f70f358486771bede4136d7eb
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/runlim.html
    icon: bi bi-globe
tldri18n_status: 2
---
# runlim

Linux의 proc 파일 시스템을 사용하여 프로그램 및 자식 프로세스의 시간 및 메모리 사용량을 샘플링하고 제한합니다.
더 많은 정보: <https://fmv.jku.at/runlim>.

- 명령의 시간 및 메모리 사용량 출력:

`runlim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어_인자</span>

- 통계를 `stdout` 대신 파일에 기록:

`runlim --output-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어_인자</span>

- 상한 시간(초 단위) 제한:

`runlim --time-limit=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">숫자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어_인자</span>

- 실시간 상한(초 단위) 제한:

`runlim --real-time-limit=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">숫자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어_인자</span>

- 공간 상한(MB 단위) 제한:

`runlim --space-limit=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">숫자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어_인자</span>
