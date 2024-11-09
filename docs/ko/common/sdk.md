---
layout: page
title: common/sdk (한국어)
description: "여러 소프트웨어 개발 키트의 병렬 버전을 관리."
content_hash: 33a2d5af47a408c56c93a18f6b48ddbf70e87592
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/sdk.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sdk.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sdk

여러 소프트웨어 개발 키트의 병렬 버전을 관리.
Java, Groovy, Scala, Kotlin, Gradle, Maven, Vert.x 등 여러 언어를 지원.
더 많은 정보: <https://sdkman.io/usage>.

- SDK 버전 설치:

`sdk install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sdk_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sdk_버전</span>

- 현재 터미널 세션에서 특정 SDK 버전 사용:

`sdk use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sdk_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sdk_버전</span>

- 사용 가능한 SDK의 안정적인 버전 표시:

`sdk current `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sdk_이름</span>

- 설치된 모든 SDK의 안정적인 버전 표시:

`sdk current`

- 사용 가능한 모든 SDK 나열:

`sdk list`

- 특정 SDK의 모든 버전 나열:

`sdk list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sdk_이름</span>

- SDK를 최신 안정 버전으로 업그레이드:

`sdk upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sdk_이름</span>

- 특정 SDK 버전 제거:

`sdk rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sdk_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sdk_버전</span>
