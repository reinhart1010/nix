---
layout: page
title: common/wikiman (English)
description: "Offline search engine for documentation."
content_hash: aa42f9f18437727c4d4e7a97f6c386d9b83dde85
last_modified_at: 2024-11-24
tldri18n_status: 2
---
# wikiman

Offline search engine for documentation.
Supports manual pages, Arch Wiki, Gentoo Wiki, FreeBSD documentation, and tldr-pages.
More information: <https://github.com/filiparag/wikiman>.

- Search for a specific topic in all installed sources:

`wikiman `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_term</span>

- Search for a topic in a specific [s]ource:

`wikiman -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_term</span>

- Search for a topic in two or more specific [s]ources:

`wikiman -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source1,source2,...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_term</span>

- List existing [S]ources:

`wikiman -S`

- Display [h]elp:

`wikiman -h`
