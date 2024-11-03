---
layout: page
title: common/pio-debug (한국어)
description: "PlatformIO 프로젝트 디버그."
content_hash: 8aa9aec9de2f3973326b9afdb719cb53c17d026e
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/pio-debug.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pio-debug.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pio debug

PlatformIO 프로젝트 디버그.
더 많은 정보: <https://docs.platformio.org/en/latest/core/userguide/cmd_debug.html>.

- 현재 디렉토리의 PlatformIO 프로젝트 디버그:

`pio debug`

- 특정 PlatformIO 프로젝트 디버그:

`pio debug --project-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/platformio_project</span>

- 특정 환경 디버그:

`pio debug --environment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">환경</span>

- 특정 설정 파일을 사용하여 PlatformIO 프로젝트 디버그:

`pio debug --project-conf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/platformio.ini</span>

- `gdb` 디버거를 사용하여 PlatformIO 프로젝트 디버그:

`pio debug --interface=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gdb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gdb_옵션</span>
