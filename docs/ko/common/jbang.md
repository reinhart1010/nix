---
layout: page
title: common/jbang (한국어)
description: "독립 실행형 소스 전용 Java 프로그램을 쉽게 생성, 편집 및 실행."
content_hash: 071ed92bf64e04ffe6317f6752b310747af3bdfc
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/jbang.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/jbang.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jbang

독립 실행형 소스 전용 Java 프로그램을 쉽게 생성, 편집 및 실행.
같이 보기: `java`.
더 많은 정보: <https://www.jbang.dev/documentation/guide/latest/cli/jbang.html>.

- 간단한 Java 클래스 초기화:

`jbang init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.java</span>

- Java 클래스 초기화 (스크립팅에 유용):

`jbang init --template=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cli</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.java</span>

- `jshell`을 사용하여 REPL 편집기에서 스크립트 및 의존성을 탐색하고 사용:

`jbang run --interactive`

- IDE에서 스크립트를 편집할 수 있도록 임시 프로젝트 설정:

`jbang edit --open=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">codium|code|eclipse|idea|netbeans|gitpod</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.java</span>

- Java 코드 스니펫 실행 (Java 9 이상):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'Files.list(Paths.get("/etc")).forEach(System.out::println);'</span>` | jbang -`

- 명령줄 애플리케이션 실행:

`jbang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.java</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수1 인수2 ...</span>

- 사용자의 `$PATH`에 스크립트 설치:

`jbang app install --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.java</span>

- `jbang`과 함께 사용할 특정 버전의 JDK 설치:

`jbang jdk install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>
