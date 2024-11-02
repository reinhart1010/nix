---
layout: page
title: common/ugrep (한국어)
description: "초고속 검색 도구로, 쿼리 TUI를 제공합니다."
content_hash: 483b3c5d0c0b77924b533f0bff571d695b671565
last_modified_at: 2024-11-02
related_topics:
  - title: Deutsch version
    url: /de/common/ugrep.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ugrep.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ugrep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ugrep

초고속 검색 도구로, 쿼리 TUI를 제공합니다.
더 많은 정보: <https://github.com/Genivia/ugrep>.

- 현재 디렉터리의 파일을 재귀적으로 검색하는 쿼리 TUI 시작 (도움말은 CTRL-Z):

`ugrep --query`

- 정규 표현식 검색 패턴이 포함된 파일을 현재 디렉터리에서 재귀적으로 검색:

`ugrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`"`

- 특정 파일 또는 특정 디렉터리의 모든 파일에서 검색하고 일치하는 줄 번호 표시:

`ugrep --line-number "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉터리</span>

- 현재 디렉터리의 모든 파일을 재귀적으로 검색하고 일치하는 파일의 이름 출력:

`ugrep --files-with-matches "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`"`

- 패턴에서 최대 3개의 추가, 누락 또는 불일치 문자가 있는 파일을 퍼지 검색:

`ugrep --fuzzy=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`"`

- 압축 파일, Zip 및 tar 아카이브를 재귀적으로 검색:

`ugrep --decompress "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`"`

- 특정 글로브 패턴과 일치하는 파일만 검색:

`ugrep --glob="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">글로브_패턴</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`"`

- C++ 소스 파일만 검색 (모든 파일 형식을 나열하려면 `--file-type=list` 사용):

`ugrep --file-type=cpp "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`"`
