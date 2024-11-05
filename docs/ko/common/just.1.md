---
layout: page
title: common/just.1 (한국어)
description: "프로젝트별 명령을 저장하고 실행."
content_hash: e9ac4d7864b6b4007e633423526e811433914b56
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/just.1.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/just.1.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/just.1.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># just

프로젝트별 명령을 저장하고 실행.
더 많은 정보: <https://github.com/casey/just>.

- justfile에서 지정된 레시피 실행:

`just `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레시피</span>

- 프로젝트 루트에 새 justfile 초기화:

`just --init`

- 기본 편집기로 justfile 편집:

`just -e`

- justfile에 있는 사용 가능한 레시피 나열:

`just -l`

- justfile 출력:

`just --dump`
