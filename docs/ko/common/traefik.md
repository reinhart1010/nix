---
layout: page
title: common/traefik (한국어)
description: "HTTP 리버스 프록시 및 로드 밸런서."
content_hash: 70d268f655b4a1d1d6d742ed0c4bbf163eb2de66
last_modified_at: 2024-11-10
related_topics:
  - title: Deutsch version
    url: /de/common/traefik.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/traefik.html
    icon: bi bi-globe
tldri18n_status: 2
---
# traefik

HTTP 리버스 프록시 및 로드 밸런서.
더 많은 정보: <https://traefik.io>.

- 기본 설정으로 서버 시작:

`traefik`

- 사용자 지정 설정 파일로 서버 시작:

`traefik --ConfigFile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">설정_파일.toml</span>

- 클러스터 모드를 활성화하여 서버 시작:

`traefik --cluster`

- 웹 UI를 활성화하여 서버 시작:

`traefik --web`
