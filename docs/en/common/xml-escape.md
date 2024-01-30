---
layout: page
title: common/xml-escape (English)
description: "Escape special XML characters, e.g. `<a1>` → `&lt;a1&gt;`."
content_hash: a5c10645bde427e8091dae67407f365e6ef884ba
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# xml escape

Escape special XML characters, e.g. `<a1>` → `&lt;a1&gt;`.
More information: <http://xmlstar.sourceforge.net/doc/xmlstarlet.pdf>.

- Escape special XML characters in a string:

`xml escape "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"><a1></span>`"`

- Escape special XML characters from `stdin`:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"><a1></span>`" | xml escape`

- Display help:

`xml escape --help`
