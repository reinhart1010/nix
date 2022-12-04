---
layout: page
title: common/xml-format (English)
description: "Format an XML document."
content_hash: 59ea3c9f57dbea172848dbf8299d023b85308cea
last_modified_at: 2022-12-04
---
# xml format

Format an XML document.
More information: <http://xmlstar.sourceforge.net/docs.php>.

- Format an XML document, indenting with tabs:

`xml format --indent-tab `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml|URI</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.xml</span>

- Format an HTML document, indenting with 4 spaces:

`xml format --html --indent-spaces `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.html|URI</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.html</span>

- Recover parsable parts of a malformed XML document, without indenting:

`xml format --recover --noindent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/malformed.xml|URI</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/recovered.xml</span>

- Format an XML document from `stdin`, removing the `DOCTYPE` declaration:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\input.xml</span>` | xml format --dropdtd > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.xml</span>

- Format an XML document, omitting the XML declaration:

`xml format --omit-decl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\input.xml|URI</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.xml</span>

- Display help for the `format` subcommand:

`xml format --help`
