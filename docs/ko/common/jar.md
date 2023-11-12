---
layout: page
title: common/jar (한국어)
description: "Java 애플리케이션/라이브러리 패키지 도구."
content_hash: 37cf026cd1319f54b0e88a02e39ef52f0fdb8fe5
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/jar.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/jar.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/jar.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jar

Java 애플리케이션/라이브러리 패키지 도구.
더 많은 정보: <https://docs.oracle.com/javase/tutorial/deployment/jar/basicsindex.html>.

- 현재 디렉터리의 모든 파일을 .jar 파일로 반복적으로 아카이브:

`jar cf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.jar</span>` *`

- .jar/.war 파일을 현재 디렉터리에 압축 해제:

`jar -xvf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.jar</span>

- .jar/.war 파일 콘텐츠 나열:

`jar tf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.jar</span>

- 자세한 출력이 포함된 .jar/.war 파일 콘텐츠 나열:

`jar tvf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.jar</span>
