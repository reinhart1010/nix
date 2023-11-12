---
layout: page
title: common/docker-logs (한국어)
description: "컨테이너 로그들을 출력한다."
content_hash: f4c7c7bce9bf5689c191d484b0148af446521b2b
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/docker-logs.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-logs.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-logs.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-logs.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-logs.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-logs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker logs

컨테이너 로그들을 출력한다.
더 많은 정보: <https://docs.docker.com/engine/reference/commandline/logs>.

- 컨테이너로부터 로그들을 출력하기:

`docker logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>

- 로그들을 출력하고 추적하기:

`docker logs -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>

- 최근 5줄만 출력하기:

`docker logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>` --tail `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- 로그들을 출력하고 타임스태프 추가하기:

`docker logs -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>

- 특정 시점의 컨테이너 실행 시점으로부터 로그 출력하기 (예시. 23m, 10s, 2013-01-02T13:23:37):

`docker logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>` --until `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시간</span>
