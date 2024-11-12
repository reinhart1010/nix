---
layout: page
title: osx/sed (한국어)
description: "스크립트 방식으로 텍스트 편집."
content_hash: 69342eb404a40f15f598c13ad972ed053bc69e05
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/sed.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/sed.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/sed.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/sed.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sed

스크립트 방식으로 텍스트 편집.
같이 보기: `awk`, `ed`.
더 많은 정보: <https://keith.github.io/xcode-man-pages/sed.1.html>.

- 모든 입력 라인에서 `apple`(기본 정규식)을 `mango`(기본 정규식)로 모두 교체하고 결과를 `stdout`에 출력:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | sed 's/apple/mango/g'`

- 특정 스크립트 [f]파일을 실행하고 결과를 `stdout`에 출력:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | sed -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트_파일.sed</span>

- 모든 입력 라인에서 `apple`(확장 정규식)을 `APPLE`(확장 정규식)로 모두 교체하고 결과를 `stdout`에 출력:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | sed -E 's/(apple)/\U\1/g'`

- 첫 번째 라인만 `stdout`에 출력:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | sed -n '1p'`

- `file` 내 모든 `apple`(기본 정규식)을 `mango`(기본 정규식)로 교체하고 원본을 `file.bak`으로 백업 저장:

`sed -i bak 's/apple/mango/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
