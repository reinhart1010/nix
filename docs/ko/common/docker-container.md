---
layout: page
title: common/docker-container (한국어)
description: "도커 컨테이너들을 관리한다."
content_hash: 2b0b2201efb3476b4343be28a2ad4aef96651010
related_topics:
  - title: Deutsch version
    url: /de/common/docker-container.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-container.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-container.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-container.html
    icon: bi bi-globe
---
# docker container

도커 컨테이너들을 관리한다.
더 많은 정보: <https://docs.docker.com/engine/reference/commandline/container/>.

- 현재 실행중인 도커 컨테이너들의 목록:

`docker container ls`

- 하나 혹은 더 많은 정지된 컨테이너들 실행하기:

`docker container start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너1_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너2_이름</span>

- 하나 혹은 더 많은 실행중인 컨테이너들 종료하기:

`docker container kill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>

- 하나 혹은 더 많은 실행중인 컨테이너들 중지하기:

`docker container stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>

- 하나 혹은 더 많은 컨테이너들 내에서 모든 프로세스들 일시중지하기:

`docker container pause `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>

- 하나 혹은 더 많은 컨테이너들에 대한 상세 정보 표시하기:

`docker container inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>

- 컨테이너의 파일 시스템을 tar 아카이브로 내보내기:

`docker container export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>

- 컨테이너의 변경점들로부터 새 이미지 생성하기:

`docker container commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>
