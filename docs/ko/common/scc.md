---
layout: page
title: common/scc (한국어)
description: "코드 라인 수를 계산합니다. Go로 작성되었습니다."
content_hash: 28e3f4b56e26b8526725d2e875e2e03f4c7c0ddd
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/scc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/scc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# scc

코드 라인 수를 계산합니다. Go로 작성되었습니다.
더 많은 정보: <https://github.com/boyter/scc>.

- 현재 디렉토리의 코드 라인 수 출력:

`scc`

- 대상 디렉토리의 코드 라인 수 출력:

`scc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 각 파일에 대한 출력 표시:

`scc --by-file`

- 특정 출력 형식을 사용하여 출력 표시 (기본값은 `tabular`):

`scc --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tabular|wide|json|csv|cloc-yaml|html|html-table</span>

- 특정 파일 확장자를 가진 파일만 계산:

`scc --include-ext `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">go,java,js</span>

- 카운트에서 제외할 디렉토리 지정:

`scc --exclude-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.git,.hg</span>

- 출력 및 정렬 기준 열로 정렬 (기본값은 파일 기준):

`scc --sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">files|name|lines|blanks|code|comments|complexity</span>

- 도움말 표시:

`scc -h`
