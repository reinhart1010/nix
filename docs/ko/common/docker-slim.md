---
layout: page
title: common/docker-slim (한국어)
description: "Docker 이미지를 분석하고 최적화."
content_hash: d0fc4d91298c784115ade0e957b32db3d27ce64f
last_modified_at: 2024-10-12
related_topics:
  - title: Deutsch version
    url: /de/common/docker-slim.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-slim.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-slim.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-slim.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker-slim

Docker 이미지를 분석하고 최적화.
더 많은 정보: <https://github.com/slimtoolkit/slim>.

- 인터랙티브 모드로 DockerSlim 시작:

`docker-slim`

- 특정 이미지에서 Docker 레이어 분석:

`docker-slim xray --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지:태그</span>

- Dockerfile 검사:

`docker-slim lint --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/Dockerfile</span>

- 분석하고 최적화된 Docker 이미지 생성:

`docker-slim build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지:태그</span>

- 하위 명령에 대한 도움말 표시:

`docker-slim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위_명령</span>` --help`
