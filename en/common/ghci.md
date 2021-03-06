---
layout: page
title: common/ghci (English)
description: "The Glasgow Haskell Compiler's interactive environment."
content_hash: 70ea74afe54c00303d2c8121752c64b0a88f189d
---
# ghci

The Glasgow Haskell Compiler's interactive environment.
More information: <https://downloads.haskell.org/ghc/latest/docs/html/users_guide/ghci.html>.

- Start a REPL (interactive shell):

`ghci`

- Start a REPL and load the specified Haskell source file:

`ghci `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_file.hs</span>

- Start a REPL and enable a language option:

`ghci -X`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">language_option</span>

- Start a REPL and enable some level of compiler warnings (e.g. `all` or `compact`):

`ghci -W`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">warning_level</span>

- Start a REPL with a colon-separated list of directories for finding source files:

`ghci -i`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory1</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory2</span>
