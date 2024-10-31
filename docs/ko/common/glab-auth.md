---
layout: page
title: common/glab-auth (한국어)
description: "GitLab 호스트로 인증."
content_hash: 229ac54abb7edb276a4d3a698f6dade805b2eddf
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/glab-auth.html
    icon: bi bi-globe
tldri18n_status: 2
---
# glab auth

GitLab 호스트로 인증.
더 많은 정보: <https://glab.readthedocs.io/en/latest/auth>.

- 대화형 프롬프트로 로그인:

`glab auth login`

- 토큰으로 로그인:

`glab auth login --token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">토큰</span>

- 인증 상태 확인:

`glab auth status`

- 특정 GitLab 인스턴스에 로그인:

`glab auth login --hostname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gitlab.example.com</span>
