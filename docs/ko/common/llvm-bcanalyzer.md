---
layout: page
title: common/llvm-bcanalyzer (한국어)
description: "LLVM Bitcode (`.bc`) 분석기."
content_hash: 5b8389bebedfb7393c2ae52953111fc037ce4c8d
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/llvm-bcanalyzer.html
    icon: bi bi-globe
tldri18n_status: 2
---
# llvm-bcanalyzer

LLVM Bitcode (`.bc`) 분석기.
더 많은 정보: <https://llvm.org/docs/CommandGuide/llvm-bcanalyzer.html>.

- Bitcode 파일에 대한 통계 출력:

`llvm-bcanalyzer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.bc</span>

- Bitcode 파일에 대한 SGML 표현과 통계 출력:

`llvm-bcanalyzer -dump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.bc</span>

- `stdin`에서 Bitcode 파일을 읽고 분석:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.bc</span>` | llvm-bcanalyzer`
