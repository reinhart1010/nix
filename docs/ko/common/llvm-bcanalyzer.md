---
layout: page
title: common/llvm-bcanalyzer (한국어)
description: "LLVM Bitcode (`.bc`) 분석기."
content_hash: 5b8389bebedfb7393c2ae52953111fc037ce4c8d
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/llvm-bcanalyzer.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/llvm-bcanalyzer.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># llvm-bcanalyzer

LLVM Bitcode (`.bc`) 분석기.
더 많은 정보: <https://llvm.org/docs/CommandGuide/llvm-bcanalyzer.html>.

- Bitcode 파일에 대한 통계 출력:

`llvm-bcanalyzer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.bc</span>

- Bitcode 파일에 대한 SGML 표현과 통계 출력:

`llvm-bcanalyzer -dump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.bc</span>

- `stdin`에서 Bitcode 파일을 읽고 분석:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.bc</span>` | llvm-bcanalyzer`
