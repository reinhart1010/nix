---
layout: page
title: linux/grub-script-check (한국어)
description: "`grub-script-check` 프로그램은 GRUB 스크립트 파일을 가져와 문법 오류를 검사합니다."
content_hash: ab0dbda29fd8822e02a23cd6ff5c53103861bc02
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/linux/grub-script-check.html
    icon: bi bi-globe
tldri18n_status: 2
---
# grub-script-check

`grub-script-check` 프로그램은 GRUB 스크립트 파일을 가져와 문법 오류를 검사합니다.
경로를 옵션이 아닌 인수로 받을 수 있습니다. 인수가 없을 경우, `stdin`에서 읽습니다.
더 많은 정보: <https://www.gnu.org/software/grub/manual/grub/html_node/Invoking-grub_002dscript_002dcheck.html>.

- 특정 스크립트 파일의 문법 오류 검사:

`grub-script-check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/grub_설정_파일</span>

- 입력을 읽은 후 각 줄을 표시:

`grub-script-check --verbose`

- 도움말 표시:

`grub-script-check --help`

- 버전 표시:

`grub-script-check --version`
