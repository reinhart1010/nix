---
layout: page
title: common/gh-codespace (한국어)
description: "GitHub에서 코드스페이스를 연결하고 관리."
content_hash: b2fd942504888c2548cb7a7164cce8c99a0083e9
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/gh-codespace.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/gh-codespace.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/gh-codespace.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gh codespace

GitHub에서 코드스페이스를 연결하고 관리.
더 많은 정보: <https://cli.github.com/manual/gh_codespace>.

- GitHub에서 코드스페이스를 대화식으로 생성:

`gh codespace create`

- 사용 가능한 모든 코드스페이스 나열:

`gh codespace list`

- SSH를 통해 코드스페이스에 대화식으로 연결:

`gh codespace ssh`

- 특정 파일을 코드스페이스로 대화식으로 전송:

`gh codespace cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_파일</span>` remote:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/원격_파일</span>

- 코드스페이스의 포트를 대화식으로 나열:

`gh codespace ports`

- 코드스페이스의 로그를 대화식으로 표시:

`gh codespace logs`

- 코드스페이스를 대화식으로 삭제:

`gh codespace delete`

- 하위 명령어에 대한 도움말 표시:

`gh codespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code|cp|create|delete|edit|...</span>` --help`
