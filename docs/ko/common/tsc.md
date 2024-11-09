---
layout: page
title: common/tsc (한국어)
description: "TypeScript 컴파일러."
content_hash: 28382985604c90f070d22c66ebd9d6a987927d97
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/tsc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tsc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tsc

TypeScript 컴파일러.
더 많은 정보: <https://www.typescriptlang.org/docs/handbook/compiler-options.html>.

- `foobar.ts` TypeScript 파일을 `foobar.js` JavaScript 파일로 컴파일:

`tsc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foobar.ts</span>

- 특정 목표 구문을 사용하여 TypeScript 파일을 JavaScript로 컴파일 (기본값은 `ES3`):

`tsc --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ES5|ES2015|ES2016|ES2017|ES2018|ESNEXT</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foobar.ts</span>

- 사용자 정의 이름으로 TypeScript 파일을 JavaScript 파일로 컴파일:

`tsc --outFile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.js</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.ts</span>

- `tsconfig.json` 파일에 정의된 TypeScript 프로젝트의 모든 `.ts` 파일 컴파일:

`tsc --build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tsconfig.json</span>

- 명령줄 옵션 및 인수를 텍스트 파일에서 가져와 컴파일러 실행:

`tsc @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수.txt</span>

- 여러 JavaScript 파일을 타입 체크하고, 오류만 출력:

`tsc --allowJs --checkJs --noEmit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">src/**/*.js</span>

- 코드가 변경될 때 자동으로 다시 컴파일하는 감시 모드에서 컴파일러 실행:

`tsc --watch`
