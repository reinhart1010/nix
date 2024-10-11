---
layout: page
title: common/dart (한국어)
description: "Dart 프로젝트 관리."
content_hash: 59d70ded25773b99ce1a5508a845badd200b05be
last_modified_at: 2024-10-11
related_topics:
  - title: Deutsch version
    url: /de/common/dart.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/dart.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/dart.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/dart.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/dart.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dart.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dart

Dart 프로젝트 관리.
더 많은 정보: <https://dart.dev/tools/dart-tool>.

- 같은 이름의 디렉터리에서 새로운 Dart 프로젝트를 초기화:

`dart create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>

- Dart 파일 실행:

`dart run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.dart</span>

- 현재 프로젝트에 대한 종속성을 다운로드:

`dart pub get`

- 현재 프로젝트에 대한 단위 테스트를 실행:

`dart test`

- null 안정성을 지원하도록 오래된 프로젝트의 의존성을 업데이트:

`dart pub upgrade --null-safety`

- Dart 파일을 기본 바이너리로 컴파일:

`dart compile exe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.dart</span>

- 현재 프로젝트에 자동 수정 사항을 적용:

`dart fix --apply`
