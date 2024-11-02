---
layout: page
title: common/pio-ci (한국어)
description: "임의의 소스 코드 구조로 PlatformIO 프로젝트를 빌드."
content_hash: 1068fe4308d0e280f075369645b1f9a8a1983b63
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/pio-ci.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pio-ci.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pio-ci.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pio ci

임의의 소스 코드 구조로 PlatformIO 프로젝트를 빌드.
소스 코드가 복사될 새로운 임시 프로젝트를 생성.
더 많은 정보: <https://docs.platformio.org/en/latest/core/userguide/cmd_ci.html>.

- 기본 시스템 임시 디렉토리에서 PlatformIO 프로젝트를 빌드하고 이후 삭제:

`pio ci `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로젝트</span>

- 특정 라이브러리를 지정하여 PlatformIO 프로젝트 빌드:

`pio ci --lib `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/라이브러리_폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로젝트</span>

- 특정 보드를 지정하여 PlatformIO 프로젝트 빌드 (`pio boards` 명령어로 모든 보드 목록 확인 가능):

`pio ci --board `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">보드</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로젝트</span>

- 특정 디렉토리에서 PlatformIO 프로젝트 빌드:

`pio ci --build-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/빌드_디렉토리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로젝트</span>

- 빌드 디렉토리를 삭제하지 않고 PlatformIO 프로젝트 빌드:

`pio ci --keep-build-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로젝트</span>

- 특정 구성 파일을 사용하여 PlatformIO 프로젝트 빌드:

`pio ci --project-conf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/platformio.ini</span>
