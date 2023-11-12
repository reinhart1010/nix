---
layout: page
title: common/docker-compose (한국어)
description: "다중 컨테이너 도커 어플리케이션 실행 및 관리."
content_hash: d8d8b5284880daea70443ddf3fd63e790daa149c
last_modified_at: 2023-11-12
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
  - title: Indonesia version
    url: /id/common/docker-compose.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-compose.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker-compose.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/docker-compose.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-compose.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-compose.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker compose

다중 컨테이너 도커 어플리케이션 실행 및 관리.
더 많은 정보: <https://docs.docker.com/compose/reference/>.

- 실행 중인 모든 컨테이너 목록 보기:

`docker compose ps`

- 현재 디렉토리의 `docker-compose.yml` 파일을 사용해 모든 컨테이너를 백그라운드에서 생성하고 실행하기:

`docker compose up --detach`

- 모든 컨테이너 실행, 필요 시 재빌드:

`docker compose up --build`

- 특정 구성 파일을 사용해 모든 컨테이너 실행:

`docker compose --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/파일명</span>` up`

- 실행 중인 모든 컨테이너 중지:

`docker compose stop`

- 모든 컨테이너, 네트워크, 이미지, 볼륨 중지 및 삭제:

`docker compose down --rmi all --volumes`

- 모든 컨테이너에 대한 로그 팔로우:

`docker compose logs --follow`

- 특정 컨테이너에 대한 로그 팔로우:

`docker compose logs --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>
