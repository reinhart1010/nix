---
layout: page
title: common/nasm (한국어)
description: "Netwide Assembler, 휴대용 80x86 어셈블러."
content_hash: 464a8e302dfcb78b8ba9f22508a02940df60bbca
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/nasm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nasm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nasm

Netwide Assembler, 휴대용 80x86 어셈블러.
더 많은 정보: <https://nasm.us>.

- `source.asm`을 (기본) raw 바이너리 형식의 바이너리 파일 `source`로 어셈블:

`nasm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.asm</span>

- `source.asm`을 지정된 형식의 바이너리 파일 `output_file`로 어셈블:

`nasm -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">형식</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.asm</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_파일</span>

- 유효한 출력 형식 목록 나열(기본 nasm 도움말 포함):

`nasm -hf`

- 어셈블하고 어셈블리 목록 파일 생성:

`nasm -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">목록_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.asm</span>

- 어셈블하기 전에 포함 파일 검색 경로에 디렉토리 추가(마지막에 슬래시 포함 필요):

`nasm -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/포함_폴더/</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.asm</span>
