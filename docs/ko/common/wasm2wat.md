---
layout: page
title: common/wasm2wat (한국어)
description: "WebAssembly 바이너리 형식을 텍스트 형식으로 변환."
content_hash: e49040f886f5f9b252c97ca5778a7d7570cbe534
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/wasm2wat.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/wasm2wat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># wasm2wat

WebAssembly 바이너리 형식을 텍스트 형식으로 변환.
더 많은 정보: <https://github.com/WebAssembly/wabt>.

- 파일을 텍스트 형식으로 변환하여 콘솔에 표시:

`wasm2wat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.wasm</span>

- 출력 결과를 지정한 파일에 저장:

`wasm2wat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.wasm</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.wat</span>
