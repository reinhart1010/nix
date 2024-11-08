---
layout: page
title: linux/coproc (한국어)
description: "상호작용 비동기 하위 셸을 생성하기 위한 Bash 내장 명령어."
content_hash: 4e7de12924aad8ea2d4035118fb0c08e0ddf71f8
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/coproc.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/coproc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/coproc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># coproc

상호작용 비동기 하위 셸을 생성하기 위한 Bash 내장 명령어.
더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#Coprocesses>.

- 하위 셸을 비동기적으로 실행:

`coproc { `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어1; 명령어2; ...</span>`; }`

- 특정 이름으로 보조 프로세스 생성:

`coproc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` { `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어1; 명령어2; ...</span>`; }`

- 특정 보조 프로세스의 `stdin`에 쓰기:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력</span>`" >&"$`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{이름</span>`[1]}"`

- 특정 보조 프로세스의 `stdout`에서 읽기:

`read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>` <&"$`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{이름</span>`[0]}"`

- `stdin`을 계속 읽고 입력에 대해 명령어를 실행하는 보조 프로세스 생성:

`coproc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` { while read line; do `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어1; 명령어2; ...</span>`; done }`

- `stdin`을 계속 읽고 입력에 대해 파이프 라인을 실행하고 출력을 `stdout`에 쓰는 보조 프로세스 생성:

`coproc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` { while read line; do echo "$line" | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어1 | 명령어2 | ...</span>` | cat /dev/fd/0; done }`

- `bc`를 실행하는 보조 프로세스를 생성하고 사용:

`coproc BC { bc --mathlib; }; echo "1/3" >&"${BC[1]}"; read output <&"${BC[0]}"; echo "$output"`
