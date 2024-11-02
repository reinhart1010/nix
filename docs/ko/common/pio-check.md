---
layout: page
title: common/pio-check (한국어)
description: "PlatformIO 프로젝트에 대한 정적 분석 검사를 수행."
content_hash: 1ba0f14d6879f51c53c13f1660ce032a3cc86ef8
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/pio-check.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pio-check.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pio-check.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pio check

PlatformIO 프로젝트에 대한 정적 분석 검사를 수행.
더 많은 정보: <https://docs.platformio.org/en/latest/core/userguide/cmd_check.html>.

- 현재 프로젝트에 대한 기본 분석 검사 수행:

`pio check`

- 특정 프로젝트에 대한 기본 분석 검사 수행:

`pio check --project-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_디렉토리</span>

- 특정 환경에 대한 분석 검사 수행:

`pio check --environment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">환경</span>

- 지정된 결함 심각도 유형만 보고하도록 분석 검사 수행:

`pio check --severity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">낮음|중간|높음</span>

- 환경을 처리할 때 상세한 정보 표시와 함께 분석 검사 수행:

`pio check --verbose`
