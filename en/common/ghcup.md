---
layout: page
title: common/ghcup (English)
description: "Haskell toolchain installer."
content_hash: d1a0a63816b87b9681681b0175447a8d2afdf8b1
---
# ghcup

Haskell toolchain installer.
Install, manage, and update Haskell toolchains.
More information: <https://gitlab.haskell.org/haskell/ghcup-hs>.

- Start the interactive TUI:

`ghcup tui`

- List available GHC/cabal versions:

`ghcup list`

- Install the recommended GHC version:

`ghcup install ghc`

- Install a specific GHC version:

`ghcup install ghc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Set the currently "active" GHC version:

`ghcup set ghc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Install cabal-install:

`ghcup install cabal`

- Update `ghcup` itself:

`ghcup upgrade`
