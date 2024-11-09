---
layout: page
title: common/topgrade (한국어)
description: "시스템의 모든 애플리케이션을 업데이트."
content_hash: 19464c2756380c7a44e1aedd80b7ef1782575ee3
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/topgrade.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/topgrade.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># topgrade

시스템의 모든 애플리케이션을 업데이트.
더 많은 정보: <https://github.com/r-darwish/topgrade>.

- 업데이트 실행:

`topgrade`

- 모든 업데이트에 대해 '예'라고 응답:

`topgrade -y`

- 임시/오래된 파일 정리:

`topgrade -c`

- 특정 업데이트 작업 비활성화:

`topgrade --disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업</span>

- 특정 업데이트 작업만 수행:

`topgrade --only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업</span>

- 기본 편집기로 구성 파일 편집:

`topgrade --edit-config`
