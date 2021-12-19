---
layout: page
title: common/docker-images (한국어)
description: "도커 이미지를 관리한다."
content_hash: 3c366073b6cf18635ac53939c69f80179070ab04
related_topics:
  - title: Deutsch version
    url: /de/common/docker-images.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-images.html
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
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/docker-images.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># docker images

도커 이미지를 관리한다.
더 많은 정보: <https://docs.docker.com/engine/reference/commandline/images/>.

- 모든 도커 이미지 목록보기:

`docker images`

- 중간자를 포함한 모든 도커 이미지 목록보기:

`docker images -a`

- 잔잔한 모드로 결과 목록보기(수로 표현된 ID들만):

`docker images -q`

- 어떠한 컨테이너에서도 사용되지 않은 모든 도커 이미지 목록보기:

`docker images --filter dangling=true`
