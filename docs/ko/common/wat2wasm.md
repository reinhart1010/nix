---
layout: page
title: common/wat2wasm (한국어)
description: "WebAssembly 텍스트 형식을 바이너리 형식으로 변환."
content_hash: 39d0a95b4022c9378c6071458fab1b6eafa1d210
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/wat2wasm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/wat2wasm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># wat2wasm

WebAssembly 텍스트 형식을 바이너리 형식으로 변환.
더 많은 정보: <https://github.com/WebAssembly/wabt>.

- 파일을 파싱하고 오류 확인:

`wat2wasm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.wat</span>

- 출력 바이너리를 지정된 파일에 저장:

`wat2wasm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.wat</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.wasm</span>

- 모든 바이트의 단순화된 표현 표시:

`wat2wasm -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.wat</span>
