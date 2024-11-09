---
layout: page
title: common/tuir (한국어)
description: "터미널에서 Reddit을 조회하고 상호작용할 수 있는 텍스트 사용자 인터페이스(TUI)."
content_hash: 5482d759e8fb4d1a946da02e3782cacca10ebfcf
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/tuir.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tuir.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tuir

터미널에서 Reddit을 조회하고 상호작용할 수 있는 텍스트 사용자 인터페이스(TUI).
Vim 키로 탐색.
더 많은 정보: <https://gitlab.com/ajak/tuir>.

- tuir 시작:

`tuir`

- 서브레딧 열기:

`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서브레딧_이름</span>

- 링크 열기:

`o`

- 시작 시 특정 서브레딧 열기:

`tuir -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서브레딧_이름</span>

- mailcap 설정에서 정의된 프로그램을 사용하여 외부 링크 열기:

`tuir --enable-media`
