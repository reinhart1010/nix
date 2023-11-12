---
layout: page
title: common/pt (English)
description: "Platinum Searcher."
content_hash: 799ec70f7566aea489b5531a042bdbfbb9280898
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# pt

Platinum Searcher.
A code search tool similar to `ag`.
More information: <https://github.com/monochromegane/the_platinum_searcher>.

- Find files containing "foo" and print the files with highlighted matches:

`pt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- Find files containing "foo" and display count of matches in each file:

`pt -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- Find files containing "foo" as a whole word and ignore its case:

`pt -wi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- Find "foo" in files with a given extension using a regular expression:

`pt -G='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\.bar$</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- Find files whose contents match the regular expression, up to 2 directories deep:

`pt --depth=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` -e '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">^ba[rz]*$</span>`'`
