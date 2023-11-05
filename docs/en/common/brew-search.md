---
layout: page
title: common/brew-search (English)
description: "Search for casks and formulae."
content_hash: 906de6a58cdb0f2fd996d5d4581216fe5a47196c
last_modified_at: 2023-11-05
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># brew search

Search for casks and formulae.
More information: <https://docs.brew.sh/Manpage#search--s-options-textregex->.

- Search for casks and formulae using a keyword:

`brew search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>

- Search for casks and formulae using a regular expression:

`brew search /`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`/`

- Enable searching through descriptions:

`brew search --desc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>

- Only search for formulae:

`brew search --formula `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>

- Only search for casks:

`brew search --cask `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>
