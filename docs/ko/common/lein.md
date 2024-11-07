---
layout: page
title: common/lein (한국어)
description: "선언적 구성을 사용하여 Clojure 프로젝트를 관리."
content_hash: 7b4887e48c1b8eadaf96bf1c4c473c26111d484f
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/lein.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/lein.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># lein

선언적 구성을 사용하여 Clojure 프로젝트를 관리.
더 많은 정보: <https://leiningen.org>.

- 템플릿을 기반으로 새 프로젝트의 구조 생성:

`lein new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">템플릿_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>

- 프로젝트와 함께 또는 독립적으로 REPL 세션 시작:

`lein repl`

- 프로젝트의 `-main` 함수와 선택적 인수 실행:

`lein run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수</span>

- 프로젝트 테스트 실행:

`lein test`

- 프로젝트 파일과 모든 의존성을 jar 파일로 패키징:

`lein uberjar`
