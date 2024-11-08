---
layout: page
title: common/llvm-dis (한국어)
description: "LLVM 비트코드 파일을 사람이 읽을 수 있는 LLVM 중간 표현(IR)로 변환."
content_hash: 50af58afa5833c4f78944da73a8724ecd78362e8
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/llvm-dis.html
    icon: bi bi-globe
tldri18n_status: 2
---
# llvm-dis

LLVM 비트코드 파일을 사람이 읽을 수 있는 LLVM 중간 표현(IR)로 변환.
더 많은 정보: <https://www.llvm.org/docs/CommandGuide/llvm-dis.html>.

- 비트코드 파일을 LLVM IR로 변환하고 결과를 `stdout`으로 출력:

`llvm-dis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.bc</span>` -o -`

- 비트코드 파일을 동일한 파일 이름의 LLVM IR 파일로 변환:

`llvm-dis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.bc</span>

- 비트코드 파일을 LLVM IR로 변환하고 결과를 지정된 파일에 기록:

`llvm-dis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.bc</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.ll</span>
