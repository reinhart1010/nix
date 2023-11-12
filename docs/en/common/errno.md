---
layout: page
title: common/errno (English)
description: "Look up errno names and descriptions."
content_hash: cd33d426fbae30399ab1836309e2cf40b5a9b431
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/common/errno.html
    icon: bi bi-globe
tldri18n_status: 2
---
# errno

Look up errno names and descriptions.
More information: <https://joeyh.name/code/moreutils/>.

- Lookup errno description by name or code:

`errno `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|code</span>

- List all errno names, codes, and descriptions:

`errno --list`

- Search for code whose description contains all of the given text:

`errno --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>

- Search for code whose description contains all of the given text (all locales):

`errno --search-all-locales `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>
