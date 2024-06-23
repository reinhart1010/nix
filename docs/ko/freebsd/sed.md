---
layout: page
title: freebsd/sed (한국어)
description: "스크립트로 텍스트를 편집합니다."
content_hash: a0ced5191f2a68a36a780f343226fbcdc337f700
last_modified_at: 2024-06-23
related_topics:
  - title: English version
    url: /en/freebsd/sed.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/freebsd/sed.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/freebsd/sed.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sed

스크립트로 텍스트를 편집합니다.
같이 보기: `awk`, `ed`.
더 많은 정보: <https://www.freebsd.org/cgi/man.cgi?sed>.

- 모든 입력 라인에서 `apple` (기본 정규표현식)을 `mango` (기본 정규표현식)로 대체하고 결과를 `stdout`에 인쇄:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` | sed 's/apple/mango/g'`

- 특정 스크립트 [f]파일을 실행하고 결과를 `stdout`에 인쇄:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` | sed -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.sed</span>

- 관련 `w` 함수 또는 플래그가 포함된 명령이 입력 줄에 적용될 때까지 각 파일 열기 지연:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` | sed -fa `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.sed</span>

- 모든 입력 라인에서 `apple` (확장 정규표현식)을 `APPLE` (확장 정규표현식)로 대체하고 결과를 `stdout`에 인쇄:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` | sed -E 's/(apple)/\U\1/g'`

- 첫 번째 줄만 `stdout`에 인쇄:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` | sed -n '1p'`

- 특정 파일에서 `apple` (기본 정규표현식)을 `mango` (기본 정규표현식)로 모두 대체하고 원본 파일 덮어쓰기:

`sed -i 's/apple/mango/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
