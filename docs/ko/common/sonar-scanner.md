---
layout: page
title: common/sonar-scanner (한국어)
description: "Maven, Gradle, Ant와 같은 빌드 도구를 사용하지 않는 SonarQube 프로젝트를 위한 일반 스캐너."
content_hash: 4cc4f9944c0e3c66b4f6504777049658080b7867
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/sonar-scanner.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sonar-scanner

Maven, Gradle, Ant와 같은 빌드 도구를 사용하지 않는 SonarQube 프로젝트를 위한 일반 스캐너.
더 많은 정보: <https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/>.

- 프로젝트의 루트 디렉토리에 있는 `sonar-project.properties`라는 구성 파일로 프로젝트 스캔:

`sonar-scanner`

- `sonar-project.properties`가 아닌 다른 구성 파일을 사용하여 프로젝트 스캔:

`sonar-scanner -D`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project.settings=myproject.properties</span>

- 디버깅 정보 출력:

`sonar-scanner -X`

- 도움말 표시:

`sonar-scanner -h`
