---
layout: page
title: common/comby (한국어)
description: "다양한 언어를 지원하는 구조적인 코드 검색 및 교체 도구."
content_hash: 6e5ff89523845702b47ed7b292f519ff924e149a
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/comby.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/comby.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># comby

다양한 언어를 지원하는 구조적인 코드 검색 및 교체 도구.
더 많은 정보: <https://github.com/comby-tools/comby>.

- 템플릿 일치 및 재작성, 변경 사항 출력:

`comby '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">assert_eq!(:[a], :[b])</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">assert_eq!(:[b], :[a])</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.rs</span>

- 일치되는 부분을 찾고, 프로퍼티에 따른 교체를 수행:

`comby '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">assert_eq!(:[a], :[b])</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">assert_eq!(:[b].Capitalize, :[a])</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.rs</span>

- 패턴과 일치하는 부분을 찾고 바로 교체:

`comby -in-place '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">일치_패턴</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">교체_패턴</span>`'`

- 패턴 검색만 수행하고 일치되는 항목을 출력:

`comby -match-only '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">일치_패턴</span>`' ""`
