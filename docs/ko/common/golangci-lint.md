---
layout: page
title: common/golangci-lint (한국어)
description: "병렬 처리, 스마트하고 빠른 Go 린터 실행 도구로 주요 IDE와 통합되며 YAML 구성을 지원합니다."
content_hash: 62df22d2ca820afc326cebcab4ae611ab79cf9f8
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/common/golangci-lint.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/golangci-lint.html
    icon: bi bi-globe
tldri18n_status: 2
---
# golangci-lint

병렬 처리, 스마트하고 빠른 Go 린터 실행 도구로 주요 IDE와 통합되며 YAML 구성을 지원합니다.
더 많은 정보: <https://golangci-lint.run/welcome/quick-start/>.

- 현재 폴더에서 린터 실행:

`golangci-lint run`

- 활성화 및 비활성화된 린터 목록 표시 (참고: 비활성화된 린터는 마지막에 표시되며, 활성화된 린터로 착각하지 마세요):

`golangci-lint linters`

- 특정 린터를 이 실행에서 [E]nable:

`golangci-lint run --enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">린터</span>
