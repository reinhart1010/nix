---
layout: page
title: common/eqn (English)
description: "Equation preprocessor for the groff (GNU Troff) document formatting system."
content_hash: dcad4bf2a7432a86777a347c3c28a6b6012c60b2
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# eqn

Equation preprocessor for the groff (GNU Troff) document formatting system.
See also `troff` and `groff`.
More information: <https://manned.org/eqn>.

- Process input with equations, saving the output for future typesetting with groff to PostScript:

`eqn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.eqn</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.roff</span>

- Typeset an input file with equations to PDF using the [me] macro package:

`eqn -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.eqn</span>` | groff -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">me</span>` -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pdf</span>
