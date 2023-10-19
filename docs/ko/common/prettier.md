---
layout: page
title: common/prettier (한국어)
description: "JavaScript, JSON, CSS, YAML 등을 위한 명시적인 코드 포맷 도구."
content_hash: e3d9308726990d8fd7bc8ded23c3cf309627804b
last_modified_at: 2023-10-19
related_topics:
  - title: English version
    url: /en/common/prettier.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># prettier

JavaScript, JSON, CSS, YAML 등을 위한 명시적인 코드 포맷 도구.
더 많은 정보: <https://prettier.io/>.

- 파일 형식을 지정하고 결과를 `stdout`으로 출력:

`prettier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 파일의 형식이 지정되었는지 확인:

`prettier --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 구성 파일로 실행:

`prettier --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/설정_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일이나 폴더를 포맷하여 원본을 대체:

`prettier --write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 작은따옴표를 사용하고 후행 쉼표를 사용하지 않고 파일 또는 폴더 형식을 반복적으로 지정:

`prettier --single-quote --trailing-comma `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">none</span>` --write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- JavaScript 및 TypeScript 파일의 형식을 재귀적으로 지정하여 원본 대체:

`prettier --write "**/*.{js,jsx,ts,tsx}"`
