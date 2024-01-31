---
layout: page
title: linux/po4a-translate (English)
description: "Convert a PO file back to documentation format."
content_hash: ec675d6d9e154b12dd79cd76740f87199cab9169
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# po4a-translate

Convert a PO file back to documentation format.
The provided PO file should be the translation of the POT file which was produced by `po4a-gettextize`.
More information: <https://po4a.org/man/man1/po4a-translate.1.php>.

- Convert a translated PO file back to a document:

`po4a-translate --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>` --master `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/master.doc</span>` --po `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/result.po</span>` --localized `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/translated.txt</span>

- List all available formats:

`po4a-translate --help-format`
