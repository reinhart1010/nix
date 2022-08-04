---
layout: page
title: common/errno (English)
description: "Look up errno names and descriptions."
content_hash: 19847bc0dfd7ce376e2e843034838387ee49a6c5
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># errno

Look up errno names and descriptions.
More information: <https://joeyh.name/code/moreutils/>.

- Lookup errno description by name or code:

`errno `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|code</span>

- List all errno names, codes, and descriptions:

`errno --list`

- Search for code who's description contains all of the given text:

`errno --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>

- Search for code who's description contains all of the given text (all locales):

`errno --search-all-locales `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>
