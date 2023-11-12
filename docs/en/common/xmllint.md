---
layout: page
title: common/xmllint (English)
description: "XML parser and linter that supports XPath, a syntax for navigating XML trees."
content_hash: 7b200fe0a7b60acc38a1f6416590d202b863866b
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# xmllint

XML parser and linter that supports XPath, a syntax for navigating XML trees.
More information: <https://manned.org/xmllint>.

- Return all nodes (tags) named "foo":

`xmllint --xpath "//`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_file.xml</span>

- Return the contents of the first node named "foo" as a string:

`xmllint --xpath "string(//`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>`)" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_file.xml</span>

- Return the href attribute of the second anchor element in an HTML file:

`xmllint --html --xpath "string(//a[2]/@href)" webpage.xhtml`

- Return human-readable (indented) XML from file:

`xmllint --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_file.xml</span>

- Check that an XML file meets the requirements of its DOCTYPE declaration:

`xmllint --valid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_file.xml</span>

- Validate XML against DTD schema hosted online:

`xmllint --dtdvalid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">URL</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_file.xml</span>
