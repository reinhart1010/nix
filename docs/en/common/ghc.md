---
layout: page
title: common/ghc (English)
description: "The Glasgow Haskell Compiler."
content_hash: 9c4564cae21e64f1a488a9dbb38da2445e5ce0cf
---
# ghc

The Glasgow Haskell Compiler.
Compiles and links Haskell source files.
More information: <https://www.haskell.org/ghc>.

- Find and compile all modules in the current directory:

`ghc Main`

- Compile a single file:

`ghc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.hs</span>

- Compile using extra optimization:

`ghc -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.hs</span>

- Stop compilation after generating object files (.o):

`ghc -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.hs</span>

- Start a REPL (interactive shell):

`ghci`

- Evaluate a single expression:

`ghc -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression</span>
