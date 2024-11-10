---
layout: page
title: linux/mpicc (한국어)
description: "Open MPI C 래퍼 컴파일러."
content_hash: d7c69fb3b737dbe4749ad77a71bbbc4b1a367121
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/mpicc.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/mpicc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mpicc

Open MPI C 래퍼 컴파일러.
래퍼는 C 컴파일러 위에 얇은 쉘로, Open MPI 프로그램을 컴파일/링크하는 데 필요한 관련 컴파일러 및 링커 플래그를 명령줄에 추가한 후, 실제 명령을 수행하기 위해 기본 C 컴파일러를 호출합니다.
더 많은 정보: <https://www.mpich.org/static/docs/latest/www1/mpicc.html>.

- 소스 코드 파일을 개체 파일로 컴파일:

`mpicc -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.c</span>

- 개체 파일을 링크하여 실행 파일 생성:

`mpicc -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">실행_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/개체_파일.o</span>

- 소스 코드를 컴파일하고 링크를 한 번에 수행:

`mpicc -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">실행_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.c</span>
