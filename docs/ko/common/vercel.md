---
layout: page
title: common/vercel (한국어)
description: "당신의 Vercel 프로젝트들을 관리하고 배포하세요."
content_hash: d42a7cf86f4b2699acd872c713d55d290dace8e8
last_modified_at: 2023-10-23
related_topics:
  - title: English version
    url: /en/common/vercel.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># vercel

당신의 Vercel 프로젝트들을 관리하고 배포하세요.
더 많은 정보: <https://vercel.com/docs/cli>.

- 현재 디렉토리를 배포:

`vercel`

- 현재 디렉토리를 프로덕션에 배포:

`vercel --prod`

- 특정 디렉토리를 배포:

`vercel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로젝트</span>

- 예제 프로젝트를 초기화:

`vercel init`

- 환경 변수와 함께 배포:

`vercel --env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ENV</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">var</span>

- 환경 변수와 함께 빌드:

`vercel --build-env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ENV</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">var</span>

- 배포를 적용할 기본 지역을 설정:

`vercel --regions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">region_id</span>

- 배포된 프로젝트를 제거:

`vercel remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>
