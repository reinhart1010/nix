---
layout: page
title: common/doctl-auth (한국어)
description: "API 토큰으로 `doctl`을 인증."
content_hash: b8af088144e49016c79b22e472f9ef3870d4a05d
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/doctl-auth.html
    icon: bi bi-globe
tldri18n_status: 2
---
# doctl auth

API 토큰으로 `doctl`을 인증.
더 많은 정보: <https://docs.digitalocean.com/reference/doctl/reference/auth/>.

- API 토큰을 입력하고 해당 컨텍스트에 라벨을 지정하라는 메시지를 열기:

`doctl auth init --context `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">토큰_라벨</span>

- 인증 컨텍스트 나열 (API 토큰):

`doctl auth list`

- 컨텍스트 전환 (API 토큰):

`doctl auth switch --context `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">토큰_라벨</span>

- 저장된 인증 컨텍스트 제거 (API 토큰):

`doctl auth remove --context `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">토큰_라벨</span>

- 사용 가능한 명령 표시:

`doctl auth --help`
