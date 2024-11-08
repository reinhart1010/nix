---
layout: page
title: common/rgrep (한국어)
description: "정규 표현식을 사용하여 파일에서 패턴을 재귀적으로 찾기."
content_hash: c25b72d9f544f2bad43bc9c2075724bfa83f21ea
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/rgrep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rgrep

정규 표현식을 사용하여 파일에서 패턴을 재귀적으로 찾기.
`grep -r`와 동일합니다.
더 많은 정보: <https://www.gnu.org/software/grep/manual/grep.html>.

- 현재 작업 디렉토리에서 패턴을 재귀적으로 검색:

`rgrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`"`

- 현재 작업 디렉토리에서 대소문자를 구분하지 않고 패턴을 재귀적으로 검색:

`rgrep --ignore-case "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`"`

- 현재 작업 디렉토리에서 확장 정규 표현식 패턴 (지원 기능: `?`, `+`, `{}`, `()` 및 `|`)을 재귀적으로 검색:

`rgrep --extended-regexp "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`"`

- 현재 작업 디렉토리에서 정확한 문자열(정규 표현식 비활성화)을 재귀적으로 검색:

`rgrep --fixed-strings "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정확한_문자열</span>`"`

- 지정된 디렉토리(또는 파일)에서 패턴을 재귀적으로 검색:

`rgrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉토리</span>
