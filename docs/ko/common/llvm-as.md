---
layout: page
title: common/llvm-as (한국어)
description: "LLVM Intermediate Representation(`.ll`)을 Bitcode(`.bc`)로 변환하는 어셈블러."
content_hash: aebb7322eda206c6333bc110bf97b2ee054e2519
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/llvm-as.html
    icon: bi bi-globe
tldri18n_status: 2
---
# llvm-as

LLVM Intermediate Representation(`.ll`)을 Bitcode(`.bc`)로 변환하는 어셈블러.
더 많은 정보: <https://llvm.org/docs/CommandGuide/llvm-as.html>.

- IR 파일을 어셈블:

`llvm-as -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.bc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스.ll</span>

- IR 파일을 어셈블하고, 생성된 Bitcode 파일에 모듈 해시 포함:

`llvm-as --module-hash -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.bc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스.ll</span>

- `stdin`에서 IR 파일을 읽어 어셈블:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스.ll</span>` | llvm-as -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.bc</span>
