---
layout: page
title: common/xml-format (English)
description: "Format an XML document."
content_hash: 2e9ce4bb013eacc427fb927ca033c85c95f83c10
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# xml format

Format an XML document.
More information: <https://xmlstar.sourceforge.net/docs.php>.

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

- Display help:

`xml format --help`
