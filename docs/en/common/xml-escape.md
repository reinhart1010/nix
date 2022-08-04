---
layout: page
title: common/xml-escape (English)
description: "Escape special XML characters, e.g. `<a1>` → `&lt;a1&gt;`."
content_hash: 85dcc15c8d3f7bb98299d6fcc59f9050b4dd5054
---
# xml escape

Escape special XML characters, e.g. `<a1>` → `&lt;a1&gt;`.
More information: <http://xmlstar.sourceforge.net/doc/xmlstarlet.pdf>.

- Escape special XML characters in a string:

`xml escape "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"><a1></span>`"`

- Escape special XML characters from stdin:

`echo  "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"><a1></span>`" | xml escape`

- Display help for the `escape` subcommand:

`xml escape --help`
