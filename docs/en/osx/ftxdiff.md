---
layout: page
title: osx/ftxdiff (English)
description: "Compare differences between two fonts."
content_hash: de485756c1693c4504c4a8bde3ea69b417681d3c
last_modified_at: 2022-12-19
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ftxdiff

Compare differences between two fonts.
More information: <https://developer.apple.com/fonts>.

- Output differences to a specific text file:

`ftxdiff --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/fontdiff.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/font1.ttc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/font2.ttc</span>

- Include glyph names in output:

`ftxdiff --include-glyph-names`

- Include unicode names in output:

`ftxdiff --include-unicode-names`
