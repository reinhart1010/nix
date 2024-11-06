---
layout: page
title: common/jhat (한국어)
description: "Java 힙 분석 도구."
content_hash: ab24bf4f28a096aae3f92569120eeed5895a54de
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/jhat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/jhat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jhat

Java 힙 분석 도구.
더 많은 정보: <https://docs.oracle.com/javase/8/docs/technotes/tools/unix/jhat.html>.

- 힙 덤프(`jmap`에서 생성)를 분석하고, HTTP를 통해 포트 7000에서 보기:

`jhat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">덤프_파일.bin</span>

- 힙 덤프를 분석하고, HTTP 서버의 대체 포트를 지정:

`jhat -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">덤프_파일.bin</span>

- 최대 8GB RAM을 사용하여 덤프를 분석 (`jhat` 사용 권장 2-4배 덤프 크기):

`jhat -J-mx8G `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">덤프_파일.bin</span>
