---
layout: page
title: common/rvm (한국어)
description: "여러 루비 환경을 쉽게 설치하고 관리하며 작업할 수 있는 도구."
content_hash: aa492185c6dc2665defd9992f64fd09328a96c51
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/rvm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/rvm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/rvm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rvm

여러 루비 환경을 쉽게 설치하고 관리하며 작업할 수 있는 도구.
더 많은 정보: <https://rvm.io>.

- 하나 이상의 루비 버전 설치:

`rvm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전1 버전2 ...</span>

- 설치된 버전 목록 표시:

`rvm list`

- 특정 루비 버전 사용:

`rvm use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 기본 루비 버전 설정:

`rvm --default use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 루비 버전을 새 버전으로 업그레이드:

`rvm upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">현재_버전</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새로운_버전</span>

- 루비 버전을 제거하고 소스는 유지:

`rvm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 루비 버전과 소스를 모두 제거:

`rvm remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 운영 체제에 대한 특정 의존성 표시:

`rvm requirements`
