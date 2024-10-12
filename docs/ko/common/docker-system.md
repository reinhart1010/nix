---
layout: page
title: common/docker-system (한국어)
description: "Docker 데이터를 관리하고 시스템 전반의 정보를 표시합니다."
content_hash: 36b81d39768fdc8fd2ce38ef9b90f2d361db5349
last_modified_at: 2024-10-12
related_topics:
  - title: Deutsch version
    url: /de/common/docker-system.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-system.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-system.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker-system.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-system.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-system.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker system

Docker 데이터를 관리하고 시스템 전반의 정보를 표시합니다.
더 많은 정보: <https://docs.docker.com/reference/cli/docker/system/>.

- 도움말 표시:

`docker system`

- Docker 디스크 사용량 표시:

`docker system df`

- 디스크 사용량에 대한 자세한 정보 표시:

`docker system df --verbose`

- 사용하지 않는 데이터 제거:

`docker system prune`

- 지정된 시간 이상 전에 생성된 사용하지 않는 데이터 제거:

`docker system prune --filter "until=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hours</span>`h`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minutes</span>`m"`

- Docker 데몬의 실시간 이벤트 표시:

`docker system events`

- 유효한 JSON 라인으로 스트리밍되는 컨테이너의 실시간 이벤트 표시:

`docker system events --filter 'type=container' --format '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json .</span>`'`

- 시스템 전반의 정보 표시:

`docker system info`
