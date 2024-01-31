---
layout: page
title: common/ghci (English)
description: "The Glasgow Haskell Compiler's interactive environment."
content_hash: 59150e309b948369b3580cbb7a3f8795ee56c9ad
last_modified_at: 2024-01-31
related_topics:
  - title: русский version
    url: /ru/common/ghci.html
    icon: bi bi-globe
tldri18n_status: 2
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

`ghci -i`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory1:path/to/directory2:...</span>
