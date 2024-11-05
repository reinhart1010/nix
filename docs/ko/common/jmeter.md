---
layout: page
title: common/jmeter (한국어)
description: "기능적 동작의 부하 테스트 및 성능 측정을 위해 설계된 오픈 소스 Java 애플리케이션."
content_hash: dd75bff6fa4628b1e58bba3455fcb198a31cd1bc
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/jmeter.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/jmeter.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># jmeter

기능적 동작의 부하 테스트 및 성능 측정을 위해 설계된 오픈 소스 Java 애플리케이션.
더 많은 정보: <https://jmeter.apache.org>.

- GUI 없이 특정 테스트 플랜 실행:

`jmeter --nongui --testfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.jmx</span>

- 특정 로그 파일을 사용하여 GUI 없이 테스트 플랜 실행:

`jmeter --nogui --testfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.jmx</span>` --logfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/로그파일.jtl</span>

- 특정 프록시를 사용하여 GUI 없이 테스트 플랜 실행:

`jmeter --nongui --testfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.jmx</span>` --proxyHost `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">127.0.0.1</span>` --proxyPort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8888</span>

- 특정 JMeter 속성을 사용하여 GUI 없이 테스트 플랜 실행:

`jmeter --jmeterproperty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>`='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>`' --nongui --testfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.jmx</span>
