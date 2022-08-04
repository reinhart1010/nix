---
layout: page
title: common/xmlto (English)
description: "Apply an XSL stylesheet to an XML document."
content_hash: 9a26181875bf5d6ea6cfaa1f13be888b91ef1089
---
# xmlto

Apply an XSL stylesheet to an XML document.
More information: <https://pagure.io/xmlto>.

- Convert a DocBook XML document to PDF format:

`xmlto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">document.xml</span>

- Convert a DocBook XML document to HTML format and store the resulting files in a separate directory:

`xmlto -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/html_files</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">document.xml</span>

- Convert a DocBook XML document to a single HTML file:

`xmlto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html-nochunks</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">document.xml</span>

- Specify a stylesheet to use while converting a DocBook XML document:

`xmlto -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stylesheet.xsl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_format</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">document.xml</span>
