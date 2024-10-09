---
layout: page
title: common/compgen (한국어)
description: "TAB 키를 두 번 누르면 호출되는 Bash의 자동 완성 명령이 내장."
content_hash: 70f64f5adc7ad0b727baa9f522952b09004194a2
last_modified_at: 2024-10-09
related_topics:
  - title: English version
    url: /en/common/compgen.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/compgen.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/compgen.html
    icon: bi bi-globe
tldri18n_status: 2
---
# compgen

TAB 키를 두 번 누르면 호출되는 Bash의 자동 완성 명령이 내장.
더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#index-compgen>.

- 실행할 수 있는 모든 명령을 나열:

`compgen -c`

- 모든 별칭을 나열:

`compgen -a`

- 실행할 수 있는 모든 기능을 나열:

`compgen -A function`

- 쉘 예약 키워드 표시:

`compgen -k`

- 'ls'로 시작하는 사용 가능한 모든 명령/별칭을 확인:

`compgen -ac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls</span>
