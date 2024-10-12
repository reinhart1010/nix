---
layout: page
title: common/docker-rmi (한국어)
description: "Docker 이미지 삭제."
content_hash: 5b50baa156460463acd24253beb3f840243af320
last_modified_at: 2024-10-12
related_topics:
  - title: Deutsch version
    url: /de/common/docker-rmi.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-rmi.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-rmi.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-rmi.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-rmi.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker rmi

Docker 이미지 삭제.
더 많은 정보: <https://docs.docker.com/reference/cli/docker/image/rm/>.

- 도움말 표시:

`docker rmi`

- 하나 이상의 이미지를 이름으로 삭제:

`docker rmi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지1 이미지2 ...</span>

- 강제로 이미지 삭제:

`docker rmi --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지</span>

- 태그되지 않은 부모 이미지를 삭제하지 않고 이미지 삭제:

`docker rmi --no-prune `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지</span>
