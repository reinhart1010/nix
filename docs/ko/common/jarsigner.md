---
layout: page
title: common/jarsigner (한국어)
description: "Java 아카이브(JAR) 파일 서명 및 검증 도구."
content_hash: d32846c1a79655704ae8727477f4e9ca9f4f4eb0
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/jarsigner.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/jarsigner.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/jarsigner.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># jarsigner

Java 아카이브(JAR) 파일 서명 및 검증 도구.
더 많은 정보: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/jarsigner.html>.

- JAR 파일 서명:

`jarsigner `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.jar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키스토어_별칭</span>

- 특정 알고리즘으로 JAR 파일 서명:

`jarsigner -sigalg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">알고리즘</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.jar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키스토어_별칭</span>

- JAR 파일의 서명 검증:

`jarsigner -verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.jar</span>
