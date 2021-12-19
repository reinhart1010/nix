---
layout: page
title: common/docker-compose (한국어)
description: "다중 도커 응용 프로그램 실행 및 관리합니다."
content_hash: 7dc40558c1da5fc31d3363922fc013d90d22429b
related_topics:
  - title: Deutsch version
    url: /de/common/docker-compose.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-compose.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/docker-compose.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-compose.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-compose.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-compose.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-compose.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/docker-compose.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># docker-compose

다중 도커 응용 프로그램 실행 및 관리합니다.
더 많은 정보: <https://docs.docker.com/compose/reference/>.

- 실행 중인 모든 컨테이너들 목록:

`docker-compose ps`

- 현재 디렉토리로로부터 `docker-compose.yml` 파일을 사용하여 백그라운드에서 모든 컨테이너들을 생성하고 실행하기:

`docker-compose up -d`

- 모든 컨테이너들을 실행하고, 필요 시 재조립:

`docker-compose up --build`

- 대체 구성 파일을 사용하여 모든 컨테이너들 실행하기:

`docker-compose --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/파일명</span>` up`

- 실행중인 모든 컨테이너들 중지하기:

`docker-compose stop`

- 모든 컨테이너들, 네트워크, 이미지, 그리고 볼륨을 중지하고 제거하기:

`docker-compose down --rmi all --volumes`

- 모든 컨테이너들에 대한 로그들 팔로우:

`docker-compose logs --follow`
