---
layout: page
title: linux/wami (한국어)
description: "작업에 적합한 프로그램을 추천하는 오픈 소스 및 사용하기 쉬운 도구."
content_hash: 17025d10f55549d2f6d6d3dc384ead40c931c7b8
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/wami.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/wami.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># wami

작업에 적합한 프로그램을 추천하는 오픈 소스 및 사용하기 쉬운 도구.
더 많은 정보: <https://github.com/evait-security/wami>.

- 모든 카테고리에서 결과를 찾아 지정된 순서로 [S]정렬:

`wami --show-all -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">asc|desc</span>` --search-all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색어</span>

- GitHub에서 확장된 결과를 찾아 내림차순으로 [S]정렬:

`wami --show-all -S desc --github `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색어</span>

- GitHub에서 검색어와 일치하는 주제 검색:

`wami --list-topics `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색어</span>

- pentest에 사용되는 도구를 검색하여 기본 자격 증명에 대해 쿼리하고 결과를 내림차순으로 [S]정렬:

`wami -S desc --search-all pentest credential default`
