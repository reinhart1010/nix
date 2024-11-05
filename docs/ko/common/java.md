---
layout: page
title: common/java (한국어)
description: "Java 애플리케이션 실행기."
content_hash: 50759a97491fefd29ad625b0b654a43bfb516238
last_modified_at: 2024-11-05
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
tldri18n_status: 2
---
# java

Java 애플리케이션 실행기.
더 많은 정보: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/java.html>.

- 메인 메서드를 포함한 Java `.class` 파일을 클래스 이름만 사용하여 실행:

`java `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클래스명</span>

- 추가 서드파티 또는 사용자 정의 클래스를 사용하여 Java 프로그램 실행:

`java -classpath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/클래스1</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/클래스2</span>`:. `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클래스명</span>

- `.jar` 프로그램 실행:

`java -jar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명.jar</span>

- 포트 5005에서 연결 대기 상태로 디버그 모드에서 `.jar` 프로그램 실행:

`java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 -jar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명.jar</span>

- JDK, JRE 및 HotSpot 버전 표시:

`java -version`

- 도움말 표시:

`java -help`
