---
layout: page
title: common/ghc (English)
description: "The Glasgow Haskell Compiler."
content_hash: 912a454dbea741d9f6c1dd596cf9fd6fc31d47c4
last_modified_at: 2023-12-27
related_topics:
  - title: русский version
    url: /ru/common/ghc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ghc

The Glasgow Haskell Compiler.
Compiles and links Haskell source files.
More information: <https://www.haskell.org/ghc>.

- Find and compile all modules in the current directory:

`ghc Main`

- Compile a single file:

`ghc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.hs</span>

- Compile using extra optimization:

`ghc -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.hs</span>

- Stop compilation after generating object files (.o):

`ghc -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.hs</span>

- Start a REPL (interactive shell):

`ghci`

- Evaluate a single expression:

`ghc -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression</span>
