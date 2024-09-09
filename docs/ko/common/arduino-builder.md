---
layout: page
title: common/arduino-builder (한국어)
description: "아두이노 스케치 컴파일."
content_hash: c673fd9c0d4c4d705b53dc92419f6383ad1cadf4
last_modified_at: 2024-09-09
related_topics:
  - title: English version
    url: /en/common/arduino-builder.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/arduino-builder.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/arduino-builder.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/arduino-builder.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/arduino-builder.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># arduino-builder

아두이노 스케치 컴파일.
사용 중단 경고: 이 도구는 `arduino`로 인해 단계적으로 중단.
더 많은 정보: <https://github.com/arduino/arduino-builder>.

- 스케치를 작성:

`arduino-builder -compile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/sketch.ino</span>

- 디버그 수준 지정 (기본값: 5):

`arduino-builder -debug-level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1..10</span>

- 사용자 정의 빌드 디렉토리 지정:

`arduino-builder -build-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/빌드_디렉터리</span>

- `-hardware`, `-tools` 등을 매번 수동으로 지정하는 대신, 빌드 옵션 파일을 사용:

`arduino-builder -build-options-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/build.options.json</span>

- 상세 모드 활성화:

`arduino-builder -verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>
