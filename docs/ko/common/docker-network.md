---
layout: page
title: common/docker-network (한국어)
description: "Docker 네트워크 생성 및 관리."
content_hash: 6d47d3bb14dbb27c039dc794e4bd54c015432665
last_modified_at: 2024-10-12
related_topics:
  - title: Deutsch version
    url: /de/common/docker-network.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-network.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-network.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-network.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-network.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-network.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker network

Docker 네트워크 생성 및 관리.
더 많은 정보: <https://docs.docker.com/reference/cli/docker/network/>.

- Docker 데몬에서 사용 가능하고 구성된 모든 네트워크 나열:

`docker network ls`

- 사용자 정의 네트워크 생성:

`docker network create --driver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">드라이버_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네트워크_이름</span>

- 하나 이상의 네트워크에 대한 자세한 정보 표시:

`docker network inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네트워크_이름1 네트워크_이름2 ...</span>

- 이름 또는 ID를 사용하여 네트워크에 컨테이너 연결:

`docker network connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네트워크_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름|ID</span>

- 네트워크에서 컨테이너 연결 해제:

`docker network disconnect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네트워크_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름|ID</span>

- 사용되지 않는 모든 네트워크 제거 (어떤 컨테이너에도 참조되지 않음):

`docker network prune`

- 하나 이상의 사용되지 않는 네트워크 제거:

`docker network rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네트워크_이름1 네트워크_이름2 ...</span>
