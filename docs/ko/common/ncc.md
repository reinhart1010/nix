---
layout: page
title: common/ncc (한국어)
description: "Node.js 애플리케이션을 단일 파일로 컴파일."
content_hash: faaa3e951017f0e6c97c87414f11a4f1f4f9bd9a
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/ncc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ncc

Node.js 애플리케이션을 단일 파일로 컴파일.
TypeScript, 바이너리 애드온 및 동적 require를 지원.
더 많은 정보: <https://github.com/vercel/ncc>.

- Node.js 애플리케이션 번들링:

`ncc build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.js</span>

- Node.js 애플리케이션을 번들링하고 축소:

`ncc build --minify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.js</span>

- Node.js 애플리케이션을 번들링하고 축소하며 소스 맵 생성:

`ncc build --source-map `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.js</span>

- 소스 파일 변경 시 자동으로 다시 컴파일:

`ncc build --watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.js</span>

- Node.js 애플리케이션을 임시 디렉토리에 번들링하고 테스트를 위해 실행:

`ncc run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.js</span>

- `ncc` 캐시 삭제:

`ncc clean cache`
