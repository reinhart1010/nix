---
layout: page
title: common/swig (한국어)
description: "C/C++ 코드와 JavaScript, Python, C# 등 다양한 고급 언어 간의 바인딩을 생성합니다."
content_hash: 0ac282e35e4ac25bfa0801aee503a785ea5a6d5c
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/swig.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/swig.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># swig

C/C++ 코드와 JavaScript, Python, C# 등 다양한 고급 언어 간의 바인딩을 생성합니다.
`.i` 또는 `.swg` 파일을 사용하여 바인딩을 생성하며, SWIG 지시어가 포함된 C/C++ 파일을 출력하여 확장 모듈을 빌드하는 데 필요한 모든 래퍼 코드를 포함합니다.
더 많은 정보: <https://www.swig.org>.

- C++와 Python 간의 바인딩 생성:

`swig -c++ -python -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_래퍼.cpp</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/swig_파일.i</span>

- C++와 Go 간의 바인딩 생성:

`swig -go -cgo -intgosize 64 -c++ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/swig_파일.i</span>

- C와 Java 간의 바인딩 생성:

`swig -java `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/swig_파일.i</span>

- C와 Ruby 간의 바인딩 생성 및 Ruby 모듈에 `foo::bar::` 접두사 추가:

`swig -ruby -prefix "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo::bar::</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/swig_파일.i</span>
