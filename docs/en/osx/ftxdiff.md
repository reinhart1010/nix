---
layout: page
title: osx/ftxdiff (English)
description: "Compare differences between two fonts."
content_hash: 5a4cb99a2ca653df8b4849bca83a25502e75148c
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/osx/ftxdiff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ftxdiff

Compare differences between two fonts.
More information: <https://developer.apple.com/fonts>.

- Output differences to a specific text file:

`ftxdiff --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/fontdiff_file.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/font_file1.ttc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/font_file2.ttc</span>

- Include glyph names in output:

`ftxdiff --include-glyph-names`

- Include unicode names in output:

`ftxdiff --include-unicode-names`
