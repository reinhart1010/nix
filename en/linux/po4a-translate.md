---
layout: page
title: linux/po4a-translate (English)
description: "Convert a PO file back to documentation format."
content_hash: f185ef901dd2104f4967d98aab5ae3bbb04741f3
---
# po4a-translate

Convert a PO file back to documentation format.
The provided PO file should be the translation of the POT file which was produced by `po4a-gettextize`.
More information: <https://po4a.org/man/man1/po4a-translate.1.php>.

- Convert a translated PO file back to a document:

`po4a-translate --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>` --master `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/master.doc</span>` --po `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/result.po</span>` --localized `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/translated.txt</span>

- Get a list of available formats:

`po4a-translate --help-format`
