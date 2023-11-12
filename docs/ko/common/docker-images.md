---
layout: page
title: common/docker-images (한국어)
description: "도커 이미지 관리."
content_hash: 0a750c8c5d7329755a2053aa550e8128aabc137a
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/docker-images.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-images.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-images.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-images.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/docker-images.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-images.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-images.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># docker images

도커 이미지 관리.
더 많은 정보: <https://docs.docker.com/engine/reference/commandline/images/>.

- 모든 도커 이미지 목록 보기:

`docker images`

- 중간 레이어를 포함한 도커 이미지 목록 보기:

`docker images --all`

- 조용한 모드로 결과 목록 보기 (이미지 ID만 출력):

`docker images --quiet`

- 어떤 컨테이너에도 사용되지 않은 도커 이미지 목록 보기:

`docker images --filter dangling=true`

- 이름에 부분 문자열을 포함한 이미지 목록 보기:

`docker images "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*이름*</span>`"`
