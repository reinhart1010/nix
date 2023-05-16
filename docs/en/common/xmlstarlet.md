---
layout: page
title: common/xmlstarlet (English)
description: "A commandline XML/XSLT toolkit."
content_hash: 9e6328eca18b5b6b2df34a7b4691f2658cca4238
last_modified_at: 2023-05-16
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># xmlstarlet

A commandline XML/XSLT toolkit.
Note: You will likely need to know XPath: <https://developer.mozilla.org/en-US/docs/Web/XPath>.
More information: <https://xmlstar.sourceforge.net/docs.php>.

- Format an XML document and print to stdout:

`xmlstarlet format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.xml</span>

- XML document can also be piped from stdin:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat path/to/file.xml</span>` | xmlstarlet format`

- Print all nodes that match a given XPath:

`xmlstarlet select --template --copy-of `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xpath</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.xml</span>

- Insert an attribute to all matching nodes, and print to stdout (source file is unchanged):

`xmlstarlet edit --insert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xpath</span>` --type attr --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">attribute_name</span>` --value `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">attribute_value</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.xml</span>

- Update the value of all matching nodes in place (source file is changed):

`xmlstarlet edit --inplace --update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xpath</span>` --value `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_value</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.xml</span>

- Delete all matching nodes in place (source file is changed):

`xmlstarlet edit --inplace --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xpath</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.xml</span>

- Escape or unescape special XML characters in a given string:

`xmlstarlet [un]escape `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>

- List a given directory as XML (omit argument to list current directory):

`xmlstarlet ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
