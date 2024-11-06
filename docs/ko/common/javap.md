---
layout: page
title: common/javap (한국어)
description: "클래스 파일을 디스어셈블하고 나열."
content_hash: 5834f6fd4bdfcadc911ebe56c87aa5ad69c7af2c
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/javap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# javap

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
