---
layout: page
title: linux/script (한국어)
description: "터미널 출력을 파일로 기록합니다."
content_hash: d279a368351a1c30067b8ceb0d13d6519cdaa597
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/script.html
    icon: bi bi-globe
tldri18n_status: 2
---
# script

터미널 출력을 파일로 기록합니다.
더 많은 정보: <https://manned.org/script>.

- 현재 디렉토리의 `typescript`라는 이름의 파일에 새 세션 기록:

`script`

- 사용자 지정 파일 경로에 새 세션 기록:

`script `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/세션.out</span>

- 기존 파일에 추가하여 새 세션 기록:

`script -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/세션.out</span>

- 타이밍 정보 기록 (`stderr`에 출력됩니다):

`script -t 2> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/타이밍_파일</span>

- 데이터가 발생하는 즉시 출력:

`script -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
