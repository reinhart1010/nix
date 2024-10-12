---
layout: page
title: common/docker-service (한국어)
description: "Docker 데몬에서 서비스를 관리합니다."
content_hash: d6690d0b5f13d452fcc6828b9131645b2a2d012f
last_modified_at: 2024-10-12
related_topics:
  - title: Deutsch version
    url: /de/common/docker-service.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-service.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-service.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-service.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-service.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker service

Docker 데몬에서 서비스를 관리합니다.
더 많은 정보: <https://docs.docker.com/reference/cli/docker/service/>.

- Docker 데몬에서 서비스 목록 나열:

`docker service ls`

- 새 서비스 생성:

`docker service create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그</span>

- 하나 이상의 서비스에 대한 자세한 정보 표시:

`docker service inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_이름_또는_ID1 서비스_이름_또는_ID2</span>

- 하나 이상의 서비스에 대한 작업 목록 나열:

`docker service ps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_이름_또는_ID1 서비스_이름_또는_ID2 ...</span>

- 공백으로 구분된 서비스 목록에 대해 특정 복제본 수로 확장:

`docker service scale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_이름</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">복제본_수</span>

- 하나 이상의 서비스 제거:

`docker service rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_이름_또는_ID1 서비스_이름_또는_ID2</span>
