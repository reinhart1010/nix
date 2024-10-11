---
layout: page
title: common/docker-ps (한국어)
description: "Docker 컨테이너 목록."
content_hash: 75ff198022ea8a1d220147ea50c06f364c802e28
last_modified_at: 2024-10-11
related_topics:
  - title: Deutsch version
    url: /de/common/docker-ps.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-ps.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-ps.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/docker-ps.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/docker-ps.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-ps.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-ps.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/docker-ps.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># docker ps

Docker 컨테이너 목록.
더 많은 정보: <https://docs.docker.com/reference/cli/docker/container/ls/>.

- 현재 실행 중인 Docker 컨테이너 목록:

`docker ps`

- 모든 Docker 컨테이너 목록 (실행 중 및 중지됨):

`docker ps --all`

- 가장 최근에 생성된 컨테이너 표시 (모든 상태 포함):

`docker ps --latest`

- 이름에 특정 문자열이 포함된 컨테이너 필터링:

`docker ps --filter "name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>`"`

- 주어진 이미지를 조상으로 공유하는 컨테이너 필터링:

`docker ps --filter "ancestor=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그</span>`"`

- 종료 상태 코드로 컨테이너 필터링:

`docker ps --all --filter="exited=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">코드</span>`"`

- 상태로 컨테이너 필터링 (created, running, removing, paused, exited, dead):

`docker ps --filter "status=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">상태</span>`"`

- 특정 볼륨을 마운트하거나 특정 경로에 볼륨이 마운트된 컨테이너 필터링:

`docker ps --filter "volume=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>`" --format "table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.ID</span>`\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Image</span>`\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Names</span>`\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Mounts</span>`"`
