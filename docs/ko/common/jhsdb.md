---
layout: page
title: common/jhsdb (한국어)
description: "Java 프로세스에 연결하거나 충돌한 Java 가상 머신의 코어 덤프를 분석하기 위해 사후 디버거를 실행."
content_hash: b0e958f5d6251c084337c79b557892a1f4d783b0
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/jhsdb.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/jhsdb.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># jhsdb

Java 프로세스에 연결하거나 충돌한 Java 가상 머신의 코어 덤프를 분석하기 위해 사후 디버거를 실행.
더 많은 정보: <https://manned.org/jhsdb>.

- Java 프로세스의 스택 및 잠금 정보 출력:

`jhsdb jstack --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- 코어 덤프를 인터랙티브 디버그 모드에서 열기:

`jhsdb clhsdb --core `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/core_dump</span>` --exe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/jdk/bin/java</span>

- 원격 디버그 서버 시작:

`jhsdb debugd --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>` --serverid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">선택적_고유_ID</span>

- 프로세스에 인터랙티브 디버그 모드로 연결:

`jhsdb clhsdb --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>
