---
layout: page
title: common/javap (한국어)
description: "클래스 파일을 디스어셈블하고 나열."
content_hash: 5834f6fd4bdfcadc911ebe56c87aa5ad69c7af2c
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/javap.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/javap.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># javap

클래스 파일을 디스어셈블하고 나열.
더 많은 정보: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/javap.html>.

- 하나 이상의 `.class` 파일을 디스어셈블하고 나열:

`javap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.class 경로/대상/파일2.class ...</span>

- 내장된 클래스 파일을 디스어셈블하고 나열:

`javap java.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>`.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클래스</span>

- 도움말 표시:

`javap -help`

- 버전 표시:

`javap -version`
