---
layout: page
title: common/pio-run (한국어)
description: "PlatformIO 프로젝트 타겟 실행."
content_hash: 2738811a9f3de8dc6419dc32791305e277effc64
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/pio-run.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pio-run.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pio run

PlatformIO 프로젝트 타겟 실행.
더 많은 정보: <https://docs.platformio.org/en/latest/core/userguide/cmd_run.html>.

- 사용 가능한 모든 프로젝트 타겟 나열:

`pio run --list-targets`

- 특정 환경의 사용 가능한 모든 프로젝트 타겟 나열:

`pio run --list-targets --environment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">환경</span>

- 모든 타겟 실행:

`pio run`

- 지정된 환경의 모든 타겟 실행:

`pio run --environment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">환경1</span>` --environment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">환경2</span>

- 특정 타겟 실행:

`pio run --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">타겟1</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">타겟2</span>

- 지정된 설정 파일의 타겟 실행:

`pio run --project-conf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/platformio.ini</span>
