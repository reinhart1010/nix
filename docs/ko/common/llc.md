---
layout: page
title: common/llc (한국어)
description: "LLVM 중간 표현(IR) 또는 비트코드를 대상에 맞는 어셈블리 언어로 컴파일합니다."
content_hash: 1481aa90bd6bb9edca09f56ef3a8299f09e6198f
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/llc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/llc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># llc

LLVM 중간 표현(IR) 또는 비트코드를 대상에 맞는 어셈블리 언어로 컴파일합니다.
더 많은 정보: <https://www.llvm.org/docs/CommandGuide/llc.html>.

- 비트코드 또는 IR 파일을 동일한 기본 이름의 어셈블리 파일로 컴파일:

`llc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ll</span>

- 모든 최적화 활성화:

`llc -O3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.ll</span>

- 특정 파일로 어셈블리 출력:

`llc --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.s</span>

- 완전히 재배치 가능하고 위치 독립적인 코드 생성:

`llc -relocation-model=pic `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.ll</span>
