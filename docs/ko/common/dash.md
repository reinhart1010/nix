---
layout: page
title: common/dash (한국어)
description: "Debian Almquist Shell은 `sh`의 최신 POSIX 호환 구현 (Bash와 호환되지 않음)."
content_hash: bd0c1abb1e2fc3f9497ddd7709935a9ebf24a133
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/dash.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/dash.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dash.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/dash.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dash

Debian Almquist Shell은 `sh`의 최신 POSIX 호환 구현 (Bash와 호환되지 않음).
더 많은 정보: <https://manned.org/dash>.

- 대화형 쉘 세션을 시작:

`dash`

- 특정 명령어([c]ommands)를 실행:

`dash -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'dash가 실행중'</span>`"`

- 특정 스크립트 실행:

`dash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.sh</span>

- 구문 오류가 있는지 특정 스크립트를 확인:

`dash -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.sh</span>

- 실행하기 전에 각 명령을 출력하는 동안 특정 스크립트를 실행:

`dash -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.sh</span>

- 특정 스크립트를 실행하고 첫 번째 오류([e]rror)에서 중지:

`dash -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.sh</span>

- `stdin`에서 특정 명령을 실행:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "echo 'dash가 실행중'"</span>` | dash`
