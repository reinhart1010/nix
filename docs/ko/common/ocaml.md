---
layout: page
title: common/ocaml (한국어)
description: "OCaml REPL (읽기-평가-출력-루프)."
content_hash: 02698c0b5d861eb857563c2a47f7cc2fff29709e
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/ocaml.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ocaml.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ocaml

OCaml REPL (읽기-평가-출력-루프).
OCaml 명령을 해석합니다.
더 많은 정보: <https://ocaml.org>.

- 사용자로부터 OCaml 명령을 입력받아 실행:

`ocaml`

- 파일에서 OCaml 명령을 읽어 실행:

`ocaml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ml</span>

- 모듈과 함께 OCaml 스크립트 실행:

`ocaml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ml</span>
