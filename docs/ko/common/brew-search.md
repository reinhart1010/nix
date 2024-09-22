---
layout: page
title: common/brew-search (한국어)
description: "casks와 formulae를 검색."
content_hash: 7153506ea94447c74c97100b54088d02ed9c8f4a
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/common/brew-search.html
    icon: bi bi-globe
tldri18n_status: 2
---
# brew search

casks와 formulae를 검색.
더 많은 정보: <https://docs.brew.sh/Manpage#search--s-options-textregex->.

- 키워드를 사용하여 casks와 formulae를 검색:

`brew search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드</span>

- 정규식을 사용하여 casks와 formulae를 검색:

`brew search /`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>`/`

- 설명을 통한 검색 활성화:

`brew search --desc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드</span>

- formulae만 검색:

`brew search --formula `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드</span>

- casks만 검색:

`brew search --cask `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드</span>
