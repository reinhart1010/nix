---
layout: page
title: common/javadoc (한국어)
description: "소스 코드에서 HTML 형식으로 Java API 문서 생성."
content_hash: e01eb74e0833b5610cd45c57424b71be4716728f
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/javadoc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/javadoc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# javadoc

소스 코드에서 HTML 형식으로 Java API 문서 생성.
더 많은 정보: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/javadoc.html>.

- Java 소스 코드에 대한 문서를 생성하고 결과를 폴더에 저장:

`javadoc -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더/</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/자바_소스코드</span>

- 특정 인코딩으로 문서 생성:

`javadoc -docencoding `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UTF-8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/자바_소스코드</span>

- 일부 패키지를 제외한 문서 생성:

`javadoc -exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_목록</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/자바_소스코드</span>
