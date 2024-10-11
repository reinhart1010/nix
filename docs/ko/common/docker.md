---
layout: page
title: common/docker (한국어)
description: "Docker 컨테이너 및 이미지를 관리."
content_hash: 3f0e29365b9bcc95f98a4094e2e51989319dff61
last_modified_at: 2024-10-11
related_topics:
  - title: Deutsch version
    url: /de/common/docker.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/docker.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/docker.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/docker.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/docker.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/docker.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker

Docker 컨테이너 및 이미지를 관리.
`run`과 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
더 많은 정보: <https://docs.docker.com/reference/cli/docker/>.

- 모든 도커 컨테이너들(실행 및 중지) 목록 보기:

`docker ps --all`

- 사용자 정의 이름으로 이미지로부터 컨테이너 실행:

`docker run --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지</span>

- 기존 컨테이너 시작 또는 중지:

`docker `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>

- 도커 레지스트리로부터 이미지 가져오기:

`docker pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지</span>

- 이미 다운로드한 이미지 목록 표시:

`docker images`

- 실행 중인 컨테이너 내부에서 Bourne 셸(`sh`)과 함께 [i]nteractive [t]ty 열기:

`docker exec -it `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sh</span>

- 중지된 컨테이너 제거:

`docker rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>

- 컨테이너의 로그 가져오기 및 실시간으로 보기:

`docker logs -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>
