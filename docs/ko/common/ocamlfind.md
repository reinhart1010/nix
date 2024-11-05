---
layout: page
title: common/ocamlfind (한국어)
description: "OCaml을 위한 findlib 패키지 관리자."
content_hash: 5d911a50497f0326e026b558a0b66cb44f6aec9c
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/ocamlfind.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ocamlfind.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ocamlfind

OCaml을 위한 findlib 패키지 관리자.
외부 라이브러리로 실행 파일을 연결하는 과정을 단순화합니다.
더 많은 정보: <https://projects.camlcity.org/projects/findlib.html>.

- 소스 파일을 네이티브 바이너리로 컴파일하고 패키지와 링크:

`ocamlfind ocamlopt -package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지1</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지2</span>` -linkpkg -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/실행파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스.ml</span>

- 소스 파일을 바이트코드 바이너리로 컴파일하고 패키지와 링크:

`ocamlfind ocamlc -package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지1</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지2</span>` -linkpkg -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/실행파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스.ml</span>

- 다른 플랫폼용으로 크로스 컴파일:

`ocamlfind -toolchain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">크로스_툴체인</span>` ocamlopt -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/실행파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스.ml</span>
