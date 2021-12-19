---
layout: page
title: linux/po4a-gettextize (English)
description: "Convert a file to a PO file."
content_hash: 463f2a00c97cc4efd3caf81b6b73e0cb3394ca02
---
# po4a-gettextize

Convert a file to a PO file.
More information: <https://po4a.org/man/man1/po4a-gettextize.1.php>.

- Convert a text file to PO file:

`po4a-gettextize --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>` --master `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/master.txt</span>` --po `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/result.po</span>

- Get a list of available formats:

`po4a-gettextize --help-format`

- Convert a text file along with a translated document to a PO file (`-l` option can be provied multiple times):

`po4a-gettextize --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>` --master `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/master.txt</span>` --localized `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/translated.txt</span>` --po `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/result.po</span>
