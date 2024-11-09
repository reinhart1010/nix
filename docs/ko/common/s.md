---
layout: page
title: common/s (한국어)
description: "터미널에서 웹 검색."
content_hash: 11949ef1cfcafa6ab1a0ae9f2e5b5cade5eb772b
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/s.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/s.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># s

터미널에서 웹 검색.
더 많은 정보: <https://github.com/zquestz/s>.

- Google(기본 제공자)에서 쿼리 검색:

`s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">쿼리</span>

- 모든 제공자 나열:

`s --list-providers`

- 지정된 제공자로 쿼리 검색:

`s --provider `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제공자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">쿼리</span>

- 지정된 바이너리를 사용하여 검색 쿼리 수행:

`s --binary "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">바이너리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">쿼리</span>
