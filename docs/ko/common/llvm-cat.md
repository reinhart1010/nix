---
layout: page
title: common/llvm-cat (한국어)
description: "LLVM 비트코드(`.bc`) 파일을 연결."
content_hash: d66ed69a96f886726282c5963e741304c4f1c157
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/llvm-cat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# llvm-cat

LLVM 비트코드(`.bc`) 파일을 연결.
더 많은 정보: <https://github.com/llvm/llvm-project/blob/main/llvm/tools/llvm-cat/llvm-cat.cpp>.

- 비트코드 파일 연결:

`llvm-cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.bc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2.bc</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.bc</span>
