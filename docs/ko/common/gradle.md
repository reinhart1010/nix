---
layout: page
title: common/gradle (한국어)
description: "오픈소스 빌드 자동화 시스템."
content_hash: 77207a1d7f117cbb314150eeb3ae120f454dfbdb
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/gradle.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/gradle.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gradle

오픈소스 빌드 자동화 시스템.
더 많은 정보: <https://gradle.org>.

- 패키지 컴파일:

`gradle build`

- 테스트 작업 제외:

`gradle build -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test</span>

- Gradle이 빌드 중에 네트워크에 접근하지 못하도록 오프라인 모드에서 실행:

`gradle build --offline`

- 빌드 디렉터리를 삭제:

`gradle clean`

- 릴리스 모드에서 Android 패키지(APK)를 빌드:

`gradle assembleRelease`

- 주요 업무를 나열:

`gradle tasks`

- 모든 작업을 나열:

`gradle tasks --all`
