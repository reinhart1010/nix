---
layout: page
title: common/wat2wasm (한국어)
description: "WebAssembly 텍스트 형식을 바이너리 형식으로 변환."
content_hash: 39d0a95b4022c9378c6071458fab1b6eafa1d210
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/wat2wasm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wat2wasm

WebAssembly 텍스트 형식을 바이너리 형식으로 변환.
더 많은 정보: <https://github.com/WebAssembly/wabt>.

- 파일을 파싱하고 오류 확인:

`wat2wasm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.wat</span>

- 출력 바이너리를 지정된 파일에 저장:

`wat2wasm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.wat</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.wasm</span>

- 모든 바이트의 단순화된 표현 표시:

`wat2wasm -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.wat</span>
