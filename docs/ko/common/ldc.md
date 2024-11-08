---
layout: page
title: common/ldc (한국어)
description: "LLVM을 백엔드로 사용하는 D 컴파일러."
content_hash: 5306781c7655d94e22b73a983d44afb6826f7633
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/ldc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ldc

LLVM을 백엔드로 사용하는 D 컴파일러.
더 많은 정보: <https://wiki.dlang.org/Using_LDC>.

- 소스 코드 파일을 실행 가능한 바이너리로 컴파일:

`ldc2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스.d</span>` -of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_실행파일</span>

- 소스 코드 파일을 링크하지 않고 컴파일:

`ldc2 -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스.d</span>

- 대상 아키텍처와 OS 선택:

`ldc -mtriple=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아키텍처_OS</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스.d</span>

- 도움말 표시:

`ldc2 -h`

- 전체 도움말 표시:

`ldc2 -help-hidden`
