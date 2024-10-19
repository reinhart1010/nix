---
layout: page
title: common/typst (English)
description: "Compile a Typst file to PDF."
content_hash: 6af99c18046fd0cce005d68dacbcf7dcbc73f65a
last_modified_at: 2024-10-19
tldri18n_status: 2
---
# typst

Compile a Typst file to PDF.
Note: Specifying the output location is optional.
More information: <https://github.com/typst/typst>.

- Initialize a new Typst project in a given directory using a template (e.g., `@preview/charged-ieee`):

`typst init "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">template</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Compile a Typst file:

`typst compile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.typ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pdf</span>

- Watch a Typst file and recompile on changes:

`typst watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.typ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pdf</span>

- List all discoverable fonts in the system and the given directory:

`typst --font-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/fonts_directory</span>` fonts`
