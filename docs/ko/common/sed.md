---
layout: page
title: common/sed (한국어)
description: "스크립트 가능한 방식으로 텍스트 편집."
content_hash: fea31d97b3b6b1bb71a1d9f9b6728dd94ee1e7fd
last_modified_at: 2024-06-13
related_topics:
  - title: dansk version
    url: /da/common/sed.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/sed.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/sed.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/sed.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sed

스크립트 가능한 방식으로 텍스트 편집.
함께 보기: `awk`, `ed`.
더 많은 정보: <https://manned.org/sed.1posix>.

- 모든 입력 줄에서 모든 `apple`(기본 정규식)항목을 `mango`(기본 정규식)로 바꾸고 결과를 `stdout`에 출력:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | sed 's/apple/mango/g'`

- 특정 스크립트 파일([f]ile)을 실행하고 결과를 `stdout`에 출력:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | sed -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/script.sed</span>

- `stdout`에 첫 번째 줄만 출력:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | sed -n '1p'`
