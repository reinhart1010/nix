---
layout: page
title: common/pio-project (한국어)
description: "PlatformIO 프로젝트 관리."
content_hash: 3df48207da0f237d48a8d3519704d492e3dca155
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/pio-project.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pio-project.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pio project

PlatformIO 프로젝트 관리.
더 많은 정보: <https://docs.platformio.org/en/latest/core/userguide/project/>.

- 새 PlatformIO 프로젝트 초기화:

`pio project init`

- 특정 디렉토리에 새 PlatformIO 프로젝트 초기화:

`pio project init --project-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로젝트_디렉토리</span>

- 보드 ID를 지정하여 새 PlatformIO 프로젝트 초기화:

`pio project init --board `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ATmega328P|uno|...</span>

- 하나 이상의 프로젝트 옵션을 지정하여 새 PlatformIO 기반 프로젝트 초기화:

`pio project init --project-option="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">옵션</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>`" --project-option="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">옵션</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>`"`

- 프로젝트 구성 출력:

`pio project config`
