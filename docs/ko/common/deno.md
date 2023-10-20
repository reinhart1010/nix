---
layout: page
title: common/deno (한국어)
description: "JavaScript 및 TypeScript를 위한 보안 런타임입니다."
content_hash: 7cea76d84132c300018b4b1b72c2eccd33bc58ef
last_modified_at: 2023-10-20
related_topics:
  - title: Deutsch version
    url: /de/common/deno.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/deno.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/deno.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/deno.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># deno

JavaScript 및 TypeScript를 위한 보안 런타임입니다.
더 많은 정보: <https://deno.land>.

- JavaScript 또는 TypeScript 파일을 실행:

`deno run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ts</span>

- REPL(대화형 쉘)을 시작:

`deno`

- 네트워크 접근이 가능한 파일을 실행:

`deno run --allow-net `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ts</span>

- URL을 통해 파일을 실행:

`deno run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://deno.land/std/examples/welcome.ts</span>

- URL을 통해 실행 가능항 스크립트 설치:

`deno install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://deno.land/std/examples/colors.ts</span>
