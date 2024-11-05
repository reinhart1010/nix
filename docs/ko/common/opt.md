---
layout: page
title: common/opt (한국어)
description: "LLVM 소스 파일을 최적화하고 분석합니다."
content_hash: ed06b758811478f551a4c6e17b61c16dcdca912f
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/opt.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/opt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># opt

LLVM 소스 파일을 최적화하고 분석합니다.
더 많은 정보: <https://llvm.org/docs/CommandGuide/opt.html>.

- 비트코드 파일에 최적화 또는 분석 실행:

`opt -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패스명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.bc</span>` -S -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_opt.bc</span>

- 함수의 제어 흐름 그래프를 `.dot` 파일로 출력:

`opt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-dot-cfg</span>` -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.bc</span>` -disable-output`

- 프로그램을 2단계로 최적화하고 결과를 다른 파일로 출력:

`opt -O2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.bc</span>` -S -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.bc</span>
