---
layout: page
title: common/wasm-opt (한국어)
description: "WebAssembly 바이너리 파일 최적화."
content_hash: fe7e59c259e2d85f3ed7c4da915a5dea913b535b
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/wasm-opt.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/wasm-opt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># wasm-opt

WebAssembly 바이너리 파일 최적화.
더 많은 정보: <https://github.com/webassembly/binaryen>.

- 기본 최적화를 적용하고 지정된 파일에 저장:

`wasm-opt -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.wasm</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.wasm</span>

- 모든 최적화를 적용하고 지정된 파일에 저장 (시간이 더 걸리지만 최적의 코드를 생성):

`wasm-opt -O4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.wasm</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.wasm</span>

- 파일을 크기 위주로 최적화:

`wasm-opt -Oz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.wasm</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.wasm</span>

- 바이너리의 텍스트 표현을 콘솔에 출력:

`wasm-opt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.wasm</span>` --print`
