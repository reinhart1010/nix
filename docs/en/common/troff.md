---
layout: page
title: common/troff (English)
description: "Typesetting processor for the groff (GNU Troff) document formatting system."
content_hash: 97ed4da8ed134effda64b4481767078ac4e5c5ad
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# troff

Typesetting processor for the groff (GNU Troff) document formatting system.
See also `groff`.
More information: <https://manned.org/troff>.

- Format output for a PostScript printer, saving the output to a file:

`troff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.roff</span>` | grops > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ps</span>

- Format output for a PostScript printer using the [me] macro package, saving the output to a file:

`troff -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">me</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.roff</span>` | grops > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ps</span>

- Format output as [a]SCII text using the [man] macro package:

`troff -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ascii</span>` -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">man</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.roff</span>` | grotty`

- Format output as a [pdf] file, saving the output to a file:

`troff -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.roff</span>` | gropdf > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pdf</span>
