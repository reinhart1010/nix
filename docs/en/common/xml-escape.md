---
layout: page
title: common/xml-escape (English)
description: "Escape special XML characters, e.g. `<a1>` → `&lt;a1&gt;`."
content_hash: 28939d2c48c5feb0e344add769851c9624a0b1af
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# xml escape

Escape special XML characters, e.g. `<a1>` → `&lt;a1&gt;`.
More information: <https://xmlstar.sourceforge.net/doc/xmlstarlet.pdf>.

- Escape special XML characters in a string:

`xml escape "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"><a1></span>`"`

- Escape special XML characters from `stdin`:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"><a1></span>`" | xml escape`

- Display help:

`xml escape --help`
