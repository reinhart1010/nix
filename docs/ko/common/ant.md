---
layout: page
title: common/ant (한국어)
description: "Apache Ant."
content_hash: aba61c444a5fdede8d937f9daf81214b71e5f338
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/ant.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ant.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ant.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ant.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ant

Apache Ant.
자바 기반 프로젝트를 빌드하고 관리하는 도구.
더 많은 정보: <https://ant.apache.org>.

- 기본 빌드 파일인 `build.xml`로 프로젝트 빌드:

`ant`

- 기본 빌드 파일인 `build.xml`이 아니라 지정된 빌드 파일로 프로젝트 빌드:

`ant -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">buildfile.xml</span>

- 이 프로젝트에 정의된 타겟들에 대한 정보 출력:

`ant -p`

- 디버깅 정보를 함께 출력:

`ant -d`

- 실패한 타겟(들)에 의존하지 않는 모든 타겟을 실행:

`ant -k`
