---
layout: page
title: osx/system_profiler (한국어)
description: "시스템 하드웨어 및 소프트웨어 구성 보고."
content_hash: c5f6d9f77a7efa3195f644468edce218e1249114
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/system_profiler.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/system_profiler.html
    icon: bi bi-globe
tldri18n_status: 2
---
# system_profiler

시스템 하드웨어 및 소프트웨어 구성 보고.
더 많은 정보: <https://keith.github.io/xcode-man-pages/system_profiler.8.html>.

- 특정 세부 수준(최소 [개인 정보 없음], 기본 또는 전체)으로 보고서 표시:

`system_profiler -detailLevel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">수준</span>

- `System Profiler.app`에서 열 수 있는 전체 시스템 프로파일러 보고서 표시:

`system_profiler -xml > MyReport.spx`

- 하드웨어 개요(모델, CPU, 메모리, 시리얼 등) 및 소프트웨어 데이터(시스템, 커널, 이름, 가동 시간 등) 표시:

`system_profiler SPHardwareDataType SPSoftwareDataType`

- 시스템 시리얼 번호 출력:

`system_profiler SPHardwareDataType|grep "Serial Number (system)" | awk '{ print $4 }'`
