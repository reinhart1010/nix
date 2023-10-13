---
layout: page
title: common/java (한국어)
description: "자바 애플리케이션 실행기."
content_hash: 1235c1a6a83b9e5f8c1c49356c845c37a00b6691
last_modified_at: 2023-10-13
related_topics:
  - title: English version
    url: /en/common/java.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/java.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/java.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/java.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/java.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/java.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># java

자바 애플리케이션 실행기.
더 많은 정보: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/java.html>.

- 클래스 이름만 사용하여 기본 메서드가 포함된 자바 클래스 파일을 실행:

`java `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클래스 이름</span>

- 자바 프로그램을 실행하고 추가적인 타사 또는 사용자 정의 클래스 사용:

`java -classpath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/classes1</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/classes2</span>`:. `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클래스 이름</span>

- `.jar` 프로그램 실행:

`java -jar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일이름.jar</span>

- 포트 5005에서 연결을 기다리는 디버그를 사용하여 `.jar` 프로그램을 실행:

`java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 -jar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일이름.jar</span>

- JDK, JRE 및 HotSpot 버전 표시:

`java -version`

- java 명령에 대한 사용법 정보 표시:

`java -help`
