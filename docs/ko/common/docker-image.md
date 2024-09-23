---
layout: page
title: common/docker-image (한국어)
description: "도커 이미지 관리."
content_hash: 7f6d10da5e1a61be8ad6f2caec6412338fbf8fe8
last_modified_at: 2024-09-23
related_topics:
  - title: Deutsch version
    url: /de/common/docker-image.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-image.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-image.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-image.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-image.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker image

도커 이미지 관리.
`docker build`, `docker import`, `docker pull` 도 확인하세요.
더 많은 정보: <https://docs.docker.com/reference/cli/docker/image/>.

- 로컬 도커 이미지 목록 보기:

`docker image ls`

- 사용되지 않는 로컬 도커 이미지 제거:

`docker image prune`

- (태그가 없는 이미지뿐만 아니라) 모든 사용되지 않는 이미지 제거:

`docker image prune --all`

- 특정 로컬 도커 이미지 히스토리 보기:

`docker image history `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지</span>
