---
layout: page
title: common/gitsome (한국어)
description: "`gh` 명령을 통해 접근할 수 있는 GitHub용 터미널 기반 인터페이스."
content_hash: e453541ddb868de7599550b5e67af0db6d59ee32
last_modified_at: 2024-10-24
related_topics:
  - title: English version
    url: /en/common/gitsome.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/gitsome.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gitsome

`gh` 명령을 통해 접근할 수 있는 GitHub용 터미널 기반 인터페이스.
또한 `git` 명령에 대한 메뉴 스타일 자동 완성 제안도 제공.
더 많은 정보: <https://github.com/donnemartin/gitsome>.

- Git (및 gh) 명령에 대한 자동 완성 및 대화형 도움말을 활성화하려면, gitsome 쉘(선택 사항)을 입력:

`gitsome`

- 현재 계정과 GitHub 통합을 설정:

`gh configure`

- 현재 계정에 대한 알림을 나열 (<https://github.com/notifications>에서 볼 수 있음):

`gh notifications`

- 주어진 검색 문자열로 필터링된, 현재 계정의 별표 표시된 저장소를 나열:

`gh starred "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">python 3</span>`"`

- 특정 GitHub 저장소의 최근 활동 피드를 보기:

`gh feed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tldr-pages/tldr</span>

- 기본 호출기(예: `less`)를 사용하여 특정 GitHub 사용자의 최근 활동 피드를 보기:

`gh feed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">torvalds</span>` -p`
