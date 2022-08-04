---
layout: page
title: common/pic (English)
description: "Picture preprocessor for the groff (GNU Troff) document formatting system."
content_hash: f4c627db5e66affde33967b46efa74d95c8c6cd4
---
# pic

Picture preprocessor for the groff (GNU Troff) document formatting system.
See also `groff` and `troff`.
More information: <https://manned.org/pic>.

- Process input with pictures, saving the output for future typesetting with groff to PostScript:

`pic `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pic</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.roff</span>

- Typeset input with pictures to PDF using the [me] macro package:

`pic -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pic</span>` | groff -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">me</span>` -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pdf</span>
