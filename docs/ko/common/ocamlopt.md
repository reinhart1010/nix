---
layout: page
title: common/ocamlopt (한국어)
description: "OCaml 네이티브 코드 컴파일러."
content_hash: 2b8184fd6307b06ecbdafb0a4cc19ba91812989e
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/ocamlopt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ocamlopt

OCaml 네이티브 코드 컴파일러.
네이티브 실행 파일을 생성합니다. 예: Linux의 ELF.
더 많은 정보: <https://ocaml.org>.

- 소스 파일 컴파일:

`ocamlopt -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_파일.ml</span>

- 디버깅을 활성화하여 컴파일:

`ocamlopt -g -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_파일.ml</span>
