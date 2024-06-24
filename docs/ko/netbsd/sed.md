---
layout: page
title: netbsd/sed (한국어)
description: "스크립트로 텍스트를 편집합니다."
content_hash: 469c4814d85a6b68341b9fa1789f0e5e9916aa16
last_modified_at: 2024-06-24
related_topics:
  - title: English version
    url: /en/netbsd/sed.html
    icon: bi bi-globe
  - title: español version
    url: /es/netbsd/sed.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/netbsd/sed.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sed

스크립트로 텍스트를 편집합니다.
같이 보기: `awk`, `ed`.
더 많은 정보: <https://man.netbsd.org/sed.1>.

- 모든 입력 라인에서 `apple` (기본 정규표현식)을 `mango` (기본 정규표현식)로 대체하고 결과를 `stdout`에 인쇄:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` | sed 's/apple/mango/g'`

- 특정 스크립트 [f]파일을 실행하고 결과를 `stdout`에 인쇄:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` | sed -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.sed</span>

- 관련 `w` 함수 또는 플래그가 포함된 명령이 입력 줄에 적용될 때까지 각 파일 열기 지연:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` | sed -fa `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.sed</span>

- GNU [g]정규식 확장 활성화:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` | sed -fg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.sed</span>

- 모든 입력 라인에서 `apple` (확장 정규표현식)을 `APPLE` (확장 정규표현식)으로 대체하고 결과를 `stdout`에 인쇄:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` | sed -E 's/(apple)/\U\1/g'`

- 첫 번째 줄만 `stdout`에 인쇄:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` | sed -n '1p'`

- 특정 파일에서 `apple` (기본 정규표현식)을 `mango` (기본 정규표현식)로 모두 대체하고 원본 파일 덮어쓰기:

`sed -i 's/apple/mango/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
