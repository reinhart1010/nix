---
layout: page
title: common/warp-diag (한국어)
description: "Cloudflare의 WARP 서비스 진단 및 피드백 도구."
content_hash: 4f532fcd478c7cf606f8a5372a6b8b8fed055e9b
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/warp-diag.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/warp-diag.html
    icon: bi bi-globe
tldri18n_status: 2
---
# warp-diag

Cloudflare의 WARP 서비스 진단 및 피드백 도구.
같이 보기: `warp-cli`.
더 많은 정보: <https://developers.cloudflare.com/warp-client/>.

- 시스템 구성 및 WARP 연결 정보가 포함된 Zip 파일 생성:

`warp-diag`

- 디버그 정보를 포함하고 출력 파일명에 타임스탬프를 추가하여 Zip 파일 생성:

`warp-diag --add-ts`

- 특정 폴더에 출력 파일 저장:

`warp-diag --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- Cloudflare의 WARP에 새로운 피드백을 대화형으로 제출:

`warp-diag feedback`
