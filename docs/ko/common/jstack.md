---
layout: page
title: common/jstack (한국어)
description: "Java 스택 추적 도구."
content_hash: 588381d19e7c8dcc51add7bb3ead0ce332463b0f
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/jstack.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jstack

Java 스택 추적 도구.
더 많은 정보: <https://manned.org/jstack>.

- Java 프로세스의 모든 스레드에 대한 Java 스택 추적 출력:

`jstack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">자바_PID</span>

- Java 프로세스의 모든 스레드에 대한 혼합 모드(Java/C++) 스택 추적 출력:

`jstack -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">자바_PID</span>

- Java 코어 덤프에서 스택 추적 출력:

`jstack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/bin/java</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.core</span>
