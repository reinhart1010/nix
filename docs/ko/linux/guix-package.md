---
layout: page
title: linux/guix-package (한국어)
description: "Guix 패키지를 설치, 업그레이드, 제거하거나 이전 구성으로 롤백합니다."
content_hash: 985fa18119fdb78c5716bef527f91f2791566c25
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/guix-package.html
    icon: bi bi-globe
tldri18n_status: 2
---
# guix package

Guix 패키지를 설치, 업그레이드, 제거하거나 이전 구성으로 롤백합니다.
더 많은 정보: <https://guix.gnu.org/manual/html_node/Invoking-guix-package.html>.

- 새 패키지 설치:

`guix package -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 제거:

`guix package -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 정규 표현식으로 패키지 데이터베이스 검색:

`guix package -s "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`"`

- 설치된 패키지 나열:

`guix package -I`

- 생성 목록 나열:

`guix package -l`

- 이전 생성으로 롤백:

`guix package --roll-back`
