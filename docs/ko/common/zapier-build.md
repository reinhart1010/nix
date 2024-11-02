---
layout: page
title: common/zapier-build (한국어)
description: "Zapier 통합의 푸시 가능한 `zip` 파일 생성."
content_hash: b49728379e60b1721e00aa710f625d4ac6d9b3ce
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/zapier-build.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zapier build

Zapier 통합의 푸시 가능한 `zip` 파일 생성.
더 많은 정보: <https://platform.zapier.com/reference/cli#build>.

- 빌드 생성:

`zapier build`

- 스마트 파일 포함 비활성화 (`index.js`에서 필요한 파일만 포함):

`zapier build --disable-dependency-detection`

- 추가 디버깅 출력 표시:

`zapier build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--debug</span>
