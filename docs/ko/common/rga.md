---
layout: page
title: common/rga (한국어)
description: "다양한 파일 유형 검색 기능을 가진 Ripgrep 래퍼."
content_hash: c24c15304054100102f318a75155aa98a3175652
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/rga.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rga

다양한 파일 유형 검색 기능을 가진 Ripgrep 래퍼.
더 많은 정보: <https://github.com/phiresky/ripgrep-all>.

- 현재 디렉토리의 모든 파일에서 패턴을 재귀적으로 검색:

`rga `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>

- 사용 가능한 어댑터 나열:

`rga --rga-list-adapters`

- 사용할 어댑터 변경 (예: ffmpeg, pandoc, poppler 등):

`rga --rga-adapters=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">어댑터1,어댑터2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>

- 파일 확장자 대신 MIME 유형을 사용하여 패턴 검색 (느림):

`rga --rga-accurate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>

- 도움말 표시:

`rga --help`
