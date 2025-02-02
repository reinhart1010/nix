---
layout: page
title: common/pv (한국어)
description: "파이프를 통해 전달되는 데이터의 진행 상황을 모니터링."
content_hash: 1f804cd29ad1946845dad26606022acaa6afe696
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/pv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pv

파이프를 통해 전달되는 데이터의 진행 상황을 모니터링.
더 많은 정보: <https://manned.org/pv>.

- 파일의 내용을 출력하고 진행 표시줄을 표시:

`pv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파이프 사이의 데이터 흐름 속도와 양을 측정 (`--size`는 선택적):

`command1 | pv --size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ETA_예상_데이터_양</span>` | command2`

- 파일을 필터링하고 진행 상황과 출력 데이터 양을 확인:

`pv -cN in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">큰_텍스트_파일</span>` | grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>` | pv -cN out > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">필터된_파일</span>

- 이미 실행 중인 프로세스에 연결하여 파일 읽기 진행 상황 보기:

`pv -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- 오류가 있는 파일을 읽고 `dd conv=sync,noerror`처럼 오류를 건너뛰기:

`pv -EE `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/오류_있는_미디어</span>` > image.img`

- 지정된 양의 데이터를 읽은 후 읽기 중지하고, 1K/s로 속도 제한:

`pv -L 1K --stop-at --size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">최대_읽기_파일_크기</span>
