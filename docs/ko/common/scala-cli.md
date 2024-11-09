---
layout: page
title: common/scala-cli (한국어)
description: "Scala 프로그래밍 언어와 상호작용."
content_hash: d113e127e5bfd968613ddc0b933926175d069ed8
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/scala-cli.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/scala-cli.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># scala-cli

Scala 프로그래밍 언어와 상호작용.
더 많은 정보: <https://scala-cli.virtuslab.org/docs/overview/>.

- 특정 Scala 버전과 JVM 버전을 사용하여 REPL(대화형 셸) 시작:

`scala-cli --scala `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3.1.0</span>` --jvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">temurin:17</span>

- Scala 스크립트 컴파일 및 실행:

`scala-cli run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.scala</span>

- Scala 스크립트 컴파일 및 테스트:

`scala-cli test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.scala</span>

- Scala 스크립트의 형식을 맞추고 파일을 직접 업데이트:

`scala-cli fmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.scala</span>

- IDE 지원을 위한 파일 생성 (VSCode 및 IntelliJ):

`scala-cli setup-ide `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.scala</span>
