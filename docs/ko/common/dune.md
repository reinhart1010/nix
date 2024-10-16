---
layout: page
title: common/dune (한국어)
description: "OCaml 프로그램용 빌드 시스템."
content_hash: ab463a3d7243b43e0932648157ebb0140f84100c
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/dune.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dune.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dune

OCaml 프로그램용 빌드 시스템.
더 많은 정보: <https://dune.build>.

- 모든 타겟 빌드:

`dune build`

- 작업 공간을 정리:

`dune clean`

- 모든 테스트 실행:

`dune runtest`

- 수동으로 로드할 필요가 없도록, 자동으로 로드된 컴파일된 모듈로 utop REPL을 시작:

`dune utop`
