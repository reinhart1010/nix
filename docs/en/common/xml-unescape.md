---
layout: page
title: common/xml-unescape (English)
description: "Unescape special XML characters, e.g. `&lt;a1&gt;` → `<a1>`."
content_hash: 817651d59a5274c46ccae0a7df79d02f6228fad7
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# xml unescape

Unescape special XML characters, e.g. `&lt;a1&gt;` → `<a1>`.
More information: <https://xmlstar.sourceforge.net/docs.php>.

- Unescape special XML characters from a string:

`xml unescape "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">&lt;a1&gt;</span>`"`

- Unescape special XML characters from `stdin`:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">&lt;a1&gt;</span>`" | xml unescape`

- Display help:

`xml escape --help`
