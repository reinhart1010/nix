---
layout: page
title: common/kotlinc (한국어)
description: "Kotlin 컴파일러."
content_hash: abbac5df62c59ae3e85ff8d042fb67fe75224688
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/kotlinc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/kotlinc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># kotlinc

Kotlin 컴파일러.
더 많은 정보: <https://kotlinlang.org/docs/command-line.html>.

- REPL (대화형 셸) 시작:

`kotlinc`

- Kotlin 파일 컴파일:

`kotlinc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.kt</span>

- 여러 Kotlin 파일 컴파일:

`kotlinc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.kt 경로/대상/파일2.kt ...</span>

- 특정 Kotlin Script 파일 실행:

`kotlinc -script `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.kts</span>

- Kotlin 파일을 Kotlin 런타임 라이브러리가 포함된 독립 실행형 jar 파일로 컴파일:

`kotlinc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.kt</span>` -include-runtime -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.jar</span>
