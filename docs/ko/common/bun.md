---
layout: page
title: common/bun (한국어)
description: "JavaScript 런타임 및 툴킷."
content_hash: 21758894dd8e3859784a27068fbd94e320398a89
last_modified_at: 2024-09-23
related_topics:
  - title: English version
    url: /en/common/bun.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/bun.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/bun.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/bun.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/bun.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bun

JavaScript 런타임 및 툴킷.
번들러, 테스트 러너 및 패키지 관리자가 포함.
더 많은 정보: <https://bun.sh>.

- JavaScript 파일 또는 `package.json` 스크립트 실행:

`bun run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일|스크립트_이름</span>

- 단위 테스트 실행:

`bun test`

- `package.json`에 종속성으로 나열된 모든 패키지를 다운로드하고 설치:

`bun install`

- `package.json`에 의존성 추가:

`bun add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>

- `package.json`로부터 의존성 제거:

`bun remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>

- 현재 디렉토리에 새로운 Bun 프로젝트 생성:

`bun init`

- REPL 시작 (대화형 쉘):

`bun repl`

- Bun을 최신버전으로 업그레이드:

`bun upgrade`
