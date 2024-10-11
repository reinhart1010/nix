---
layout: page
title: common/docker-swarm (한국어)
description: "컨테이너 오케스트레이션 도구."
content_hash: 52af00a50743e7e3545b0fff28a7e4084fb95ec8
last_modified_at: 2024-10-11
related_topics:
  - title: Deutsch version
    url: /de/common/docker-swarm.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-swarm.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-swarm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-swarm.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-swarm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/docker-swarm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># docker swarm

컨테이너 오케스트레이션 도구.
더 많은 정보: <https://docs.docker.com/engine/swarm/>.

- 스웜 클러스터 초기화:

`docker swarm init`

- 매니저 또는 워커에 합류할 수 있는 토큰 표시:

`docker swarm join-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">worker|manager</span>

- 새로운 노드를 클러스터에 합류:

`docker swarm join --token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">토큰</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">매니저_노드_url:2377</span>

- 스웜에서 워커 제거 (워커 노드 내부에서 실행):

`docker swarm leave`

- 현재 CA 인증서를 PEM 형식으로 표시:

`docker swarm ca`

- 현재 CA 인증서를 갱신하고 새 인증서 표시:

`docker swarm ca --rotate`

- 노드 인증서의 유효 기간 변경:

`docker swarm update --cert-expiry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시간</span>`h`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">분</span>`m`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">초</span>`s`
