---
layout: page
title: common/wikiman (English)
description: "Offline search engine for documentation."
content_hash: cda9f2571dc5b87fa016f1fd4f3a50817541e2ed
last_modified_at: 2024-11-23
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/wikiman.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># wikiman

Offline search engine for documentation.
Supports manual pages, Arch Wiki, Gentoo Wiki, FreeBSD documentation, and tldr-pages.
More information: <https://github.com/filiparag/wikiman>.

- Search for a specific topic on all installed sources:

`wikiman `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_term</span>

- Search for a topic in a specific [s]ource:

`wikiman -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_term</span>

- Search for a topic in two or more specific [s]ources:

`wikiman -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source1,source2,...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_term</span>

- List existing [S]ources:

`wikiman -S`

- Display [h]elp:

`wikiman -h`
