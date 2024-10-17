---
layout: page
title: common/dua (한국어)
description: "Dua (Disk Usage Analyzer): 디렉터리의 디스크 공간 사용량을 가져옴."
content_hash: 7b2447801eab79e6a7e5b30b675719765510d7a3
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/dua.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/dua.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dua

Dua (Disk Usage Analyzer): 디렉터리의 디스크 공간 사용량을 가져옴.
더 많은 정보: <https://github.com/Byron/dua-cli>.

- 특정 디렉터리 분석:

`dua `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 디스크 사용량 대신 실제로 파일에 있는 유효한 데이터 크기로 표시:

`dua --apparent-size`

- 하드 링크된 파일이 표시될 때마다, 개수를 계산:

`dua --count-hard-links`

- 하나 이상의 디렉터리 또는 파일이 소비한 공간을 집계:

`dua aggregate`

- 터미널 사용자 인터페이스 실행:

`dua interactive`

- 바이트 수를 형식에 맞게 출력:

`dua --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">metric|binary|bytes|GB|GiB|MB|MiB</span>

- 특정 스레드 수 사용(기본값은 프로세스 스레드 수):

`dua --threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>
