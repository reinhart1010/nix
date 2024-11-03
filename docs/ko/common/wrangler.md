---
layout: page
title: common/wrangler (한국어)
description: "Cloudflare Workers 명령줄 도구."
content_hash: 2207404f6ff72f7407b004141515740cfb2caf2f
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/wrangler.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wrangler

Cloudflare Workers 명령줄 도구.
더 많은 정보: <https://developers.cloudflare.com/workers/>.

- 기본 구성으로 프로젝트 초기화:

`wrangler init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>

- Cloudflare에 인증:

`wrangler login`

- 로컬 개발 서버 시작:

`wrangler dev --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>

- 워커 스크립트 배포:

`wrangler publish`

- 프로덕션 워커의 로그 집계:

`wrangler tail`
