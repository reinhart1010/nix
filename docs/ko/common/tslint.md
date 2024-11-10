---
layout: page
title: common/tslint (한국어)
description: "TypeScript를 위한 플러그 가능한 린트 유틸리티."
content_hash: 8d4d5b24a2ef428e4008d708ef5263624d8652ba
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/tslint.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tslint

TypeScript를 위한 플러그 가능한 린트 유틸리티.
더 많은 정보: <https://palantir.github.io/tslint>.

- TSLint 구성 생성:

`tslint --init`

- 주어진 파일 집합에 대해 린트 수행:

`tslint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.js 경로/대상/파일2.js ...</span>

- 린트 문제 수정:

`tslint --fix`

- 프로젝트 루트에 있는 설정 파일로 린트 수행:

`tslint --project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로젝트_루트</span>
