---
layout: page
title: common/xml-escape (English)
description: "Escape special XML characters, e.g. `<a1>` → `&lt;a1&gt;`."
content_hash: 43a638bc070f3b441432e91fb306315f56745d96
last_modified_at: 2022-12-04
---
# xml escape

Escape special XML characters, e.g. `<a1>` → `&lt;a1&gt;`.
More information: <http://xmlstar.sourceforge.net/doc/xmlstarlet.pdf>.

- Escape special XML characters in a string:

`xml escape "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"><a1></span>`"`

- Escape special XML characters from `stdin`:

`echo  "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"><a1></span>`" | xml escape`

- Display help for the `escape` subcommand:

`xml escape --help`
