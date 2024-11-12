---
layout: page
title: osx/mas (한국어)
description: "Mac App Store용 명령줄 인터페이스."
content_hash: 61021e6a66e2d9b82e75037b5a6e5551b29e1b0d
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/mas.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/mas.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/mas.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mas

Mac App Store용 명령줄 인터페이스.
더 많은 정보: <https://github.com/mas-cli/mas>.

- Mac App Store에 처음으로 로그인:

`mas signin "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user@example.com</span>`"`

- 설치된 모든 애플리케이션과 그 제품 식별자 표시:

`mas list`

- 애플리케이션 검색 및 결과와 함께 가격 표시:

`mas search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션</span>`" --price`

- 정확한 숫자 ID를 사용하여 애플리케이션 설치 또는 업데이트:

`mas install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">숫자_제품_ID</span>

- 검색에서 반환되는 첫 번째 애플리케이션 설치:

`mas lucky "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색어</span>`"`

- 업데이트가 필요한 모든 구버전 앱 나열:

`mas outdated`

- 모든 대기 중인 업데이트 설치:

`mas upgrade`

- 특정 애플리케이션 업그레이드:

`mas upgrade "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">숫자_제품_ID</span>`"`
