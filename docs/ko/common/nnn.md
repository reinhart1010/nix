---
layout: page
title: common/nnn (한국어)
description: "인터랙티브 터미널 파일 관리 및 디스크 사용량 분석기."
content_hash: 02f55c39759522fc984f574970b1e52f4d5e5dc4
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/nnn.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/nnn.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nnn

인터랙티브 터미널 파일 관리 및 디스크 사용량 분석기.
더 많은 정보: <https://github.com/jarun/nnn>.

- 현재 디렉토리 열기 (또는 첫 번째 인수로 지정된 디렉토리 열기):

`nnn`

- 상세 모드로 시작:

`nnn -d`

- 숨김 파일 표시:

`nnn -H`

- 기존 북마크 열기 (`NNN_BMS` 환경 변수에 정의됨):

`nnn -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">북마크_이름</span>

- 파일을 [a]pparent 디스크 사용량 / [d]isk 사용량 / [e]xtension / [r]everse / [s]ize / [t]ime / [v]ersion 기준으로 정렬:

`nnn -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a|d|e|r|s|t|v</span>

- 선택한 파일 열기. 파일을 선택한 후 `o`를 누르고 파일을 열 프로그램을 입력:

`nnn -o`
