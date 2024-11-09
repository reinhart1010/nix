---
layout: page
title: common/ts-node (한국어)
description: "TypeScript 코드를 컴파일 없이 직접 실행."
content_hash: dba577bfc6dd4c437aaa94ca436ca5abeffbd145
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/ts-node.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ts-node.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ts-node

TypeScript 코드를 컴파일 없이 직접 실행.
더 많은 정보: <https://typestrong.org/ts-node>.

- TypeScript 파일을 컴파일 없이 실행 (`node` + `tsc`):

`ts-node `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ts</span>

- `tsconfig.json`을 로드하지 않고 TypeScript 파일 실행:

`ts-node --skip-project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ts</span>

- 리터럴로 전달된 TypeScript 코드 평가:

`ts-node --eval '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">console.log("Hello World")</span>`'`

- 스크립트 모드로 TypeScript 파일 실행:

`ts-node --script-mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ts</span>

- TypeScript 파일을 실행하지 않고 JavaScript로 트랜스파일:

`ts-node --transpile-only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ts</span>

- TS-Node 도움말 표시:

`ts-node --help`
