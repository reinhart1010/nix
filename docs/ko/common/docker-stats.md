---
layout: page
title: common/docker-stats (한국어)
description: "컨테이너의 리소스 사용 통계를 실시간 스트림으로 표시."
content_hash: 822fc64e92a909b6410f4f4289a28d30def341e8
last_modified_at: 2024-10-12
related_topics:
  - title: Deutsch version
    url: /de/common/docker-stats.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-stats.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-stats.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-stats.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-stats.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker stats

컨테이너의 리소스 사용 통계를 실시간 스트림으로 표시.
더 많은 정보: <https://docs.docker.com/reference/cli/docker/container/stats/>.

- 실행 중인 모든 컨테이너의 통계를 실시간 스트림으로 표시:

`docker stats`

- 하나 이상의 컨테이너에 대한 통계를 실시간 스트림으로 표시:

`docker stats `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너1 컨테이너2 ...</span>

- 컨테이너의 CPU 사용률을 표시하도록 열 형식을 변경:

`docker stats --format "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Name</span>`:\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.CPUPerc</span>`"`

- 모든 컨테이너(실행 중 및 중지된)의 통계를 표시:

`docker stats --all`

- 스트리밍 통계를 비활성화하고 현재 통계만 가져오기:

`docker stats --no-stream`
