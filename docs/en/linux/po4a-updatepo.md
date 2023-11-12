---
layout: page
title: linux/po4a-updatepo (English)
description: "Update the translation (in PO format) of a documentation."
content_hash: ef7a3eacdd6ab02da62273726abc0c3a8fb433b1
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# po4a-updatepo

Update the translation (in PO format) of a documentation.
More information: <https://po4a.org/man/man1/po4a-updatepo.1.php>.

- Update a PO file according to the modification of its origin file:

`po4a-updatepo --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>` --master `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/master.txt</span>` --po `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/result.po</span>

- Get a list of available formats:

`po4a-updatepo --help-format`

- Update several PO files according to the modification of their origin file:

`po4a-updatepo --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>` --master `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/master.txt</span>` --po `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/po1.po</span>` --po `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/po2.po</span>
