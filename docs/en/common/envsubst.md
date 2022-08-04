---
layout: page
title: common/envsubst (English)
description: "Substitutes environment variables with their value in shell format strings."
content_hash: fb3d2419b56e2d3b91623fb6a9d884286fcc886f
related_topics:
  - title: italiano version
    url: /it/common/envsubst.html
    icon: bi bi-globe
---
# envsubst

Substitutes environment variables with their value in shell format strings.
Variables to be replaced should be in either `${var}` or `$var` format.
More information: <https://www.gnu.org/software/gettext/manual/html_node/envsubst-Invocation.html>.

- Replace environment variables in stdin and output to stdout:

`echo '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$HOME</span>`' | envsubst`

- Replace environment variables in an input file and output to stdout:

`envsubst < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>

- Replace environment variables in an input file and output to a file:

`envsubst < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- Replace environment variables in an input file from a space-separated list:

`envsubst '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$USER $SHELL $HOME</span>`' < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>
