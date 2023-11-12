---
layout: page
title: common/dlv (English)
description: "Debugger for the Go programming language."
content_hash: ce4b05aa5d39c58540428e78e9578cf7915fe7d5
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# dlv

Debugger for the Go programming language.
More information: <https://github.com/go-delve/delve/blob/master/Documentation/usage/dlv.md>.

- Compile and begin debugging the main package in the current directory (by default, with no arguments):

`dlv debug`

- Compile and begin debugging a specific package:

`dlv debug `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arguments</span>

- Compile a test binary and begin debugging the compiled program:

`dlv test`

- Connect to a headless debug server:

`dlv connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>

- Attach to a running process and begin debugging:

`div attach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Compile and begin tracing a program:

`dlv trace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --regexp '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`'`
