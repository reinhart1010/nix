---
layout: page
title: common/shfmt (English)
description: "Shell parser, formatter and interpreter."
content_hash: 4d3e1a54b7338d10bcd9471c97359e0dc1bc252c
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# shfmt

Shell parser, formatter and interpreter.
More information: <https://pkg.go.dev/mvdan.cc/sh>.

- Print a formatted version of a shell script:

`shfmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- List unformatted files:

`shfmt --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Write the result to the file instead of printing it to the terminal:

`shfmt --write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Simplify the code, removing redundant pieces of syntax (i.e. removing "$" from vars in expressions):

`shfmt --simplify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
