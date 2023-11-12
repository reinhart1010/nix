---
layout: page
title: linux/po4a-gettextize (English)
description: "Convert a file to a PO file."
content_hash: 6a4023885d033e67842d31989d2c5349a72f4b74
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# po4a-gettextize

Convert a file to a PO file.
More information: <https://po4a.org/man/man1/po4a-gettextize.1.php>.

- Convert a text file to PO file:

`po4a-gettextize --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>` --master `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/master.txt</span>` --po `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/result.po</span>

- Get a list of available formats:

`po4a-gettextize --help-format`

- Convert a text file along with a translated document to a PO file (`-l` option can be provided multiple times):

`po4a-gettextize --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>` --master `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/master.txt</span>` --localized `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/translated.txt</span>` --po `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/result.po</span>
