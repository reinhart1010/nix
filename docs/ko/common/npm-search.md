---
layout: page
title: common/npm-search (한국어)
description: "`npm` 레지스트리에서 패키지를 검색."
content_hash: f4eb8a2fc947ddba40e332c23887d83716bd82c0
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/npm-search.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/npm-search.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># npm search

`npm` 레지스트리에서 패키지를 검색.
더 많은 정보: <https://docs.npmjs.com/cli/commands/npm-search>.

- 이름으로 패키지 검색:

`npm search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 특정 키워드로 패키지 검색:

`npm search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드</span>

- 패키지 검색 시 상세 정보 포함 (예: 설명, 작성자, 버전):

`npm search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` --long`

- 특정 작성자가 관리하는 패키지 검색:

`npm search --author `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작성자</span>

- 특정 조직의 패키지 검색:

`npm search --scope `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">조직</span>

- 특정 조합의 용어로 패키지 검색:

`npm search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">용어1 용어2 ...</span>
