---
layout: page
title: common/jenv (한국어)
description: "\"JAVA_HOME\" 환경 변수를 관리."
content_hash: 361790a3bd7523f595b9ab082b4b2d32a6b27cd2
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/jenv.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/jenv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jenv

"JAVA_HOME" 환경 변수를 관리.
더 많은 정보: <https://www.jenv.be/>.

- Java 버전을 jEnv에 추가:

`jenv add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/jdk_home</span>

- 사용 중인 현재 JDK 버전 표시:

`jenv version`

- 관리 중인 모든 JDK 표시:

`jenv versions`

- 전역 JDK 버전 설정:

`jenv global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java_버전</span>

- 현재 셸 세션에 대한 JDK 버전 설정:

`jenv shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java_버전</span>

- jEnv 플러그인 활성화:

`jenv enable-plugin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">플러그인_이름</span>
