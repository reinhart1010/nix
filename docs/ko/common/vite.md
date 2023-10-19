---
layout: page
title: common/vite (한국어)
description: "Vite 프로젝트 생성합니다."
content_hash: 47ffc6787cf70b3702ce873eea7643d3affd9a97
last_modified_at: 2023-10-19
related_topics:
  - title: English version
    url: /en/common/vite.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># Vite

Vite 프로젝트 생성합니다.
자바스크립트 프로젝트를 빌드하는 데 사용됩니다.
사용 가능한 템플릿: vanilla, vanilla-ts, vue, vue-ts, react, react-ts, react-swc, react-swc-ts, preact, preact-ts, lit, lit-ts, svelte, svelte-ts.
더 많은 정보: <https://vitejs.dev/guide>.

- `npm` 6.x를 사용한 설정:

`npm create vite@latest my-react-app --template react-ts`

- `npm` 7 이상을 사용한 설정, 추가 이중 대시가 필요:

`npm create vite@latest my-react-app -- --template react-ts`

- `yarn`을 사용한 설정:

`yarn create vite my-react-app --template react-ts`

- `pnpm`을 사용한 설정:

`pnpm create vite my-react-app --template react-ts`
