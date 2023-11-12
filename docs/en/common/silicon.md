---
layout: page
title: common/silicon (English)
description: "Create an image of source code."
content_hash: 5da07a37f712de46a821996ecb07dbb3eb2e2e2d
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# silicon

Create an image of source code.
More information: <https://github.com/Aloxaf/silicon>.

- Generate an image from a specific source file:

`silicon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_file</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_image</span>

- Generate an image from a source file with a specific programming language syntax highlighting (e.g. `rust`, `py`, `js`, etc.):

`silicon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_file</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_image</span>` --language `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">language|extension</span>

- Generate an image from `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | silicon --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_image</span>
