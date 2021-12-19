---
layout: page
title: common/docker-machine (한국어)
description: "도커를 실행하는 머신들을 생성하고 관리한다."
content_hash: 3a2bccfcac047f2d7e0071f01c5e1b5ae7ba73e3
related_topics:
  - title: Deutsch version
    url: /de/common/docker-machine.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-machine.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-machine.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-machine.html
    icon: bi bi-globe
---
# docker-machine

도커를 실행하는 머신들을 생성하고 관리한다.
더 많은 정보: <https://docs.docker.com/machine/reference/>.

- 현재 실행중인 도커 머신들 목록보기:

`docker-machine ls`

- 특정 이름으로 새로운 도커 머신 생성하기:

`docker-machine create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 머신의 상태 가져오기:

`docker-machine status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 머신 시작하기:

`docker-machine start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 머신 중지하기:

`docker-machine stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 머신에 대한 정보 검사하기:

`docker-machine inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>
