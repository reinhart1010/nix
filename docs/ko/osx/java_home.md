---
layout: page
title: osx/java_home (한국어)
description: "$JAVA_HOME의 값을 반환하거나 이 변수를 사용하여 명령을 실행합니다."
content_hash: 96ce3c705438f0e3fc4c37c5233a0bfbe70ec296
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/java_home.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/java_home.html
    icon: bi bi-globe
tldri18n_status: 2
---
# java_home

$JAVA_HOME의 값을 반환하거나 이 변수를 사용하여 명령을 실행합니다.
더 많은 정보: <https://www.unix.com/man-page/osx/1/java_home>.

- 특정 버전에 기반한 JVM 목록 나열:

`java_home --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.5+</span>

- 특정 [arch]아키텍처에 기반한 JVM 목록 나열:

`java_home --arch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">i386</span>

- 특정 작업에 기반한 JVM 목록 나열 (기본값은 `CommandLine`):

`java_home --datamodel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Applets|WebStart|BundledApp|JNI|CommandLine</span>

- XML 형식으로 JVM 목록 나열:

`java_home --xml`

- 도움말 표시:

`java_home --help`
