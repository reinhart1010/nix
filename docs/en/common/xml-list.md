---
layout: page
title: common/xml-list (English)
description: "List a directory's contents (like `ls`) in XML format."
content_hash: 2ae92a991ef8533ca906c547caa286110adc0a7b
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# xml list

List a directory's contents (like `ls`) in XML format.
More information: <http://xmlstar.sourceforge.net/docs.php>.

- Write the current directory's listing to an XML document:

`xml list > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/dir_list.xml</span>

- Write the specified directory's listing to an XML document:

`xml list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/dir_list.xml</span>

- Display help for the `list` subcommand:

`xml list --help`
