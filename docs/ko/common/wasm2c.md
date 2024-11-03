---
layout: page
title: common/wasm2c (한국어)
description: "WebAssembly 바이너리 형식을 C 소스 파일 및 헤더로 변환."
content_hash: d48d46147cf0529fbb7eb7f39d23b6022a297ff5
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/wasm2c.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wasm2c

WebAssembly 바이너리 형식을 C 소스 파일 및 헤더로 변환.
더 많은 정보: <https://github.com/WebAssembly/wabt>.

- 파일을 C 소스 파일 및 헤더로 변환하고 콘솔에 표시:

`wasm2c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.wasm</span>

- 출력 내용을 지정된 파일에 저장 (`file.h`도 추가로 생성됨):

`wasm2c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.wasm</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.c</span>
