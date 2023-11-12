---
layout: page
title: common/carp (English)
description: "REPL and build tool for Carp."
content_hash: c47d49b0a319b8d4d950049e10aae0dff75a9d2e
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# carp

REPL and build tool for Carp.
More information: <https://carp-lang.github.io/carp-docs/Manual.html>.

- Start a REPL (interactive shell):

`carp`

- Start a REPL with a custom prompt:

`carp --prompt "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">> </span>`"`

- Build a `carp` file:

`carp -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.carp</span>

- Build and run a file:

`carp -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.carp</span>

- Build a file with optimizations enabled:

`carp -b --optimize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.carp</span>

- Transpile a file to C code:

`carp --generate-only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.carp</span>
