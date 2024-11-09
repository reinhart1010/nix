---
layout: page
title: common/sbt (한국어)
description: "Scala 및 Java 프로젝트를 위한 빌드 도구."
content_hash: 391a795d91fa476613d59a0b15e302e86273848b
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/sbt.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sbt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sbt

Scala 및 Java 프로젝트를 위한 빌드 도구.
더 많은 정보: <https://www.scala-sbt.org/1.x/docs/>.

- REPL(대화형 셸) 시작:

`sbt`

- GitHub에 호스팅된 기존 Giter8 템플릿에서 새 Scala 프로젝트 생성:

`sbt new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">scala/hello-world.g8</span>

- 모든 테스트 컴파일 및 실행:

`sbt test`

- `target` 디렉토리의 모든 생성된 파일 삭제:

`sbt clean`

- `src/main/scala` 및 `src/main/java` 디렉토리의 주요 소스 컴파일:

`sbt compile`

- 지정된 버전의 sbt 사용:

`sbt -sbt-version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 특정 jar 파일을 sbt 실행 파일로 사용:

`sbt -sbt-jar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로</span>

- 모든 sbt 옵션 나열:

`sbt -h`
