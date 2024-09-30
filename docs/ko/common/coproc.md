---
layout: page
title: common/coproc (한국어)
description: "대화형 비동기 서브셸을 생성하기 위한 내장 Bash."
content_hash: e26a47aa365d827e70438cd8241d532187b5bd63
last_modified_at: 2024-09-30
related_topics:
  - title: English version
    url: /en/common/coproc.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/coproc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# coproc

대화형 비동기 서브셸을 생성하기 위한 내장 Bash.
더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#Coprocesses>.

- 서브셸을 비동기적으로 실행:

`coproc { `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어1; 명령어2; ...</span>`; }`

- 특정 이름을 가진 보조 프로세스를 만듬:

`coproc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` { `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어1; 명령어2; ...</span>`; }`

- 특정 보조 프로세스 `stdin`에 쓰기:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력</span>`" >&"$`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{이름</span>`[1]}"`

- 특정 보조 프로세스 `stdout`에서 읽음:

`read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>` <&"$`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{이름</span>`[0]}"`

- `stdin`을 반복적으로 읽고 입력에 대해 일부 명령을 실행하는 보조 프로세스를 만듬:

`coproc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` { while read line; do `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어1; 명령어2; ...</span>`; done }`

- `bc`를 실행하는 보조 프로세스를 만들고 사용:

`coproc BC { bc --mathlib; }; echo "1/3" >&"${BC[1]}"; read output <&"${BC[0]}"; echo "$output"`
