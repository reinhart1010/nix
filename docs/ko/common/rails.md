---
layout: page
title: common/rails (한국어)
description: "서버 측 MVC 프레임워크로, Ruby로 작성되었습니다."
content_hash: d70e21c4b01b4a60b3dab9a44244226a75844401
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/rails.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/rails.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/rails.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/rails.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># rails

서버 측 MVC 프레임워크로, Ruby로 작성되었습니다.
`generate`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
더 많은 정보: <https://guides.rubyonrails.org/command_line.html>.

- 새 Rails 프로젝트 생성:

`rails new "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>`"`

- 현재 프로젝트의 로컬 서버를 포트 3000에서 시작:

`rails server`

- 현재 프로젝트의 로컬 서버를 지정된 포트에서 시작:

`rails server -p "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>`"`

- 명령줄에서 애플리케이션과 상호작용할 수 있는 콘솔 열기:

`rails console`

- 현재 Rails 버전 확인:

`rails --version`
