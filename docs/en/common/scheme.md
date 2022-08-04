---
layout: page
title: common/scheme (English)
description: "MIT Scheme language interpreter and REPL (interactive shell)."
content_hash: ac66ad783db9f8fd42080735acd622abeb35117d
---
# scheme

MIT Scheme language interpreter and REPL (interactive shell).
More information: <https://www.gnu.org/software/mit-scheme>.

- Start a REPL (interactive shell):

`scheme`

- Run a scheme program (with no REPL output):

`scheme --quiet < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script.scm</span>

- Load a scheme program into the REPL:

`scheme --load `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script.scm</span>

- Load scheme expressions into the REPL:

`scheme --eval "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">(define foo 'x)</span>`"`

- Open the REPL in quiet mode:

`scheme --quiet`
