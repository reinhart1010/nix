---
layout: page
title: common/bash (한국어)
description: "Bourne-Again SHell, an `sh`- 호환 명령 행 인터프리터."
content_hash: 8812ee75bf4b07787dc38cdbc753754ca4607530
last_modified_at: 2023-12-29
related_topics:
  - title: Deutsch version
    url: /de/common/bash.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/bash.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/bash.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/bash.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bash.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/bash.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/bash.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/bash.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/bash.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># bash

Bourne-Again SHell, an `sh`- 호환 명령 행 인터프리터.
참조 : `zsh`, `histexpand` (history expansion).
더 많은 정보: <https://www.gnu.org/software/bash/>.

- 대화형 쉘 시작하기:

`bash`

- 설정 파일 로딩 없이 대화형 쉘 시작하기:

`bash --norc`

- 특정 명령어([c]ommands) 실행하기:

`bash -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'bash가 실행되었습니다'</span>`"`

- 특정 스크립트 실행하기:

`bash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/script.sh</span>

- 각 명령어 실행 전 명령어 인쇄하며 특정 스크립트 실행하기:

`bash -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/script.sh</span>

- 첫 번째 에러([e]rror)가 발생하면 중지되도록 하며 특정 스크립트 실행하기:

`bash -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/script.sh</span>

- `stdin`에서 bash 실행하기:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "echo 'bash가 실행되었습니다'"</span>` | bash`
