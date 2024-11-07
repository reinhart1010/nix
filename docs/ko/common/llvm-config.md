---
layout: page
title: common/llvm-config (한국어)
description: "LLVM을 사용하는 프로그램을 컴파일하는 데 필요한 다양한 구성 정보를 얻습니다."
content_hash: f5520258265f327f929993093d0e632d429660b2
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/llvm-config.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/llvm-config.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># llvm-config

LLVM을 사용하는 프로그램을 컴파일하는 데 필요한 다양한 구성 정보를 얻습니다.
일반적으로 Makefile이나 configure 스크립트와 같은 빌드 시스템에서 호출됩니다.
더 많은 정보: <https://llvm.org/docs/CommandGuide/llvm-config.html>.

- LLVM 기반 프로그램을 컴파일하고 링크:

`clang++ $(llvm-config --cxxflags --ldflags --libs) --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_실행파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스.cc</span>

- LLVM 설치의 `PREFIX` 출력:

`llvm-config --prefix`

- LLVM 빌드에서 지원하는 모든 대상 출력:

`llvm-config --targets-built`
