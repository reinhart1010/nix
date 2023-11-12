---
layout: page
title: common/typst (English)
description: "Compile a Typst file to PDF."
content_hash: 49c70c7ef1389ba32bb96e685896c5ec103b5123
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# typst

Compile a Typst file to PDF.
Note: Specifying the output location is optional.
More information: <https://github.com/typst/typst>.

- List all discoverable fonts in the system and the given directory:

`typst --font-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/fonts_directory</span>` fonts`

- Compile a Typst file:

`typst compile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.typ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pdf</span>

- Watch a Typst file and recompile on changes:

`typst watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.typ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pdf</span>
