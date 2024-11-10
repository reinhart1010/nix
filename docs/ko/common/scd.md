---
layout: page
title: common/scd (한국어)
description: "셸 통합에 중점을 둔 파일 관리자."
content_hash: bb594b3c9f6d851bd1063c9343c2087eea5e9cbe
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/scd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# scd

셸 통합에 중점을 둔 파일 관리자.
더 많은 정보: <https://github.com/cshuaimin/scd>.

- 처음 실행 시 경로를 재귀적으로 색인:

`scd -ar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 특정 디렉토리로 이동:

`scd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 특정 패턴과 일치하는 경로로 이동:

`scd "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴1 패턴2 ...</span>`"`

- 선택 메뉴 및 20개의 가장 가능성 높은 디렉토리 순위 표시:

`scd -v`

- 현재 디렉토리에 특정 별칭 추가:

`scd --alias=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">단어</span>

- 특정 별칭을 사용하여 디렉토리로 이동:

`scd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">단어</span>
