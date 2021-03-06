---
layout: page
title: common/xml-unescape (English)
description: "Unescape special XML characters, e.g. `&lt;a1&gt;` → `<a1>`."
content_hash: 84cf012b04436994aa7a945ef7089cd592dc9944
---
# xml unescape

Unescape special XML characters, e.g. `&lt;a1&gt;` → `<a1>`.
More information: <http://xmlstar.sourceforge.net/docs.php>.

- Unescape special XML characters from a string:

`xml unescape "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">&lt;a1&gt;</span>`"`

- Unescape special XML characters from stdin:

`echo  "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">&lt;a1&gt;</span>`" | xml unescape`

- Display help for the `unescape` subcommand:

`xml escape --help`
