---
layout: page
title: common/xcaddy (한국어)
description: "Caddy 웹 서버를 위한 커스텀 빌드 도구."
content_hash: ee72c55661914ea1169996887d115a01694da668
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/xcaddy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xcaddy

Caddy 웹 서버를 위한 커스텀 빌드 도구.
더 많은 정보: <https://github.com/caddyserver/xcaddy>.

- 소스에서 Caddy 서버 빌드:

`xcaddy build`

- 특정 버전으로 Caddy 서버 빌드 (기본값은 최신 버전):

`xcaddy build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 특정 모듈로 Caddy 빌드:

`xcaddy build --with `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>

- 특정 파일에 출력하여 Caddy 빌드:

`xcaddy build --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 현재 디렉토리에서 개발 플러그인을 위해 Caddy 빌드 및 실행:

`xcaddy run`

- 특정 Caddy 설정을 사용하여 개발 플러그인을 위해 Caddy 빌드 및 실행:

`xcaddy run --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
