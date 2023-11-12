---
layout: page
title: common/dexter (한국어)
description: "OpenId Connect를 사용하여 Kubectl 사용자를 인증하는 도구."
content_hash: 5947cf0ab353442185e1d7d59ba4690eb38be8ea
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/dexter.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dexter.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dexter

OpenId Connect를 사용하여 Kubectl 사용자를 인증하는 도구.
더 많은 정보: <https://github.com/gini/dexter>.

- Google OIDC로 사용자 생성 및 인증:

`dexter auth -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클라이언트_아이디</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클라이언트_secret</span>

- 기본 kube 구성파일 위치 재정의:

`dexter auth -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클라이언트_아이디</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클라이언트_secret</span>` --kube-config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">예시/구성파일</span>
