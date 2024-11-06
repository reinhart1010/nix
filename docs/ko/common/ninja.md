---
layout: page
title: common/ninja (한국어)
description: "빠른 빌드를 위해 설계된 빌드 시스템."
content_hash: f531c54ded3ae5a8d289d68cbc8105b0058b8b2e
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/ninja.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ninja.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ninja

빠른 빌드를 위해 설계된 빌드 시스템.
더 많은 정보: <https://ninja-build.org/manual.html>.

- 현재 디렉토리에서 빌드:

`ninja`

- 현재 디렉토리에서 빌드하고, 동시에 4개의 작업을 병렬로 실행:

`ninja -j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- 주어진 디렉토리에서 프로그램 빌드:

`ninja -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 대상 표시 (예: `install` 및 `uninstall`):

`ninja -t targets`

- 도움말 표시:

`ninja -h`
