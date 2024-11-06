---
layout: page
title: common/ocamlc (한국어)
description: "OCaml 바이트코드 컴파일러."
content_hash: bf57911eba2ec600bd1005e992acb3b0306f2128
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/ocamlc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ocamlc

OCaml 바이트코드 컴파일러.
OCaml 인터프리터로 실행 가능한 실행 파일을 생성합니다.
더 많은 정보: <https://ocaml.org>.

- 소스 파일로부터 바이너리 생성:

`ocamlc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_파일.ml</span>

- 소스 파일로부터 이름이 지정된 바이너리 생성:

`ocamlc -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_파일.ml</span>

- 자동으로 모듈 시그니처(인터페이스) 파일 생성:

`ocamlc -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_파일.ml</span>
