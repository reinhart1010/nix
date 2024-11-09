---
layout: page
title: common/tre (한국어)
description: "현재 디렉토리의 내용을 트리 형태로 표시."
content_hash: 73fb7bfee5f10b018491398824b988aeb496dc26
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/tre.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tre.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tre

현재 디렉토리의 내용을 트리 형태로 표시.
기본적으로 `.gitignore` 설정을 존중합니다.
더 많은 정보: <https://github.com/dduan/tre>.

- 디렉토리만 출력:

`tre --directories`

- 트리 구조 대신 파일을 포함한 JSON 출력:

`tre --json`

- 지정된 깊이 제한까지 파일 및 디렉토리 출력 (1은 현재 디렉토리를 의미):

`tre --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">깊이</span>

- 지정된 색상 모드를 사용하여 모든 숨김 파일 및 디렉토리 출력:

`tre --all --color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">automatic|always|never</span>

- 트리 구조 내 파일들을 출력하고, 각 파일을 연관된 `command`(기본값은 `$EDITOR`)로 열 수 있는 셸 별칭 할당:

`tre --editor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 제공된 정규 표현식과 일치하는 모든 경로를 제외하고 트리 구조 내 파일 출력:

`tre --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>

- 버전 표시:

`tre --version`

- 도움말 표시:

`tre --help`
