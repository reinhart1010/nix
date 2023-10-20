---
layout: page
title: common/javac (한국어)
description: "자바 애플리케이션 컴파일러."
content_hash: 69ebf67280da0c88ba5cc6597a005efb62b211ae
last_modified_at: 2023-10-20
related_topics:
  - title: English version
    url: /en/common/javac.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/javac.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/javac.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/javac.html
    icon: bi bi-globe
---
# javac

자바 애플리케이션 컴파일러.
더 많은 정보: <https://docs.oracle.com/en/java/javase/20/docs/specs/man/javac.html>.

- `.java` 파일을 컴파일:

`javac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.java</span>

- 여러 개의 `.java` 파일들을 컴파일:

`javac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일1.java</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일2.java</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일3.java</span>

- 현재 디렉토리 내의 모든 `.java` 파일들을 컴파일:

`javac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.java</span>

- `.java` 파일을 컴파일한 후, 결과 `.class` 파일을 특정 디렉토리에 위치시키기:

`javac -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.java</span>
