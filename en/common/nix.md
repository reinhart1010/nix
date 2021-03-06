---
layout: page
title: common/nix (English)
description: "Utilities for the Nix language and store."
content_hash: d712ffe2ebaa30ae30e38201bdd7733a6c61807a
---
# nix

Utilities for the Nix language and store.
More information: <https://nixos.org>.

- Search for a package via its name or description:

`nix search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_term</span>

- Start a Nix shell with the specified packages available:

`nix run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nixpkgs.pkg1 nixpkgs.pkg2 nixpkgs.pkg3...</span>

- Optimise Nix store disk usage by combining duplicate files:

`nix store optimise`

- Start an interactive environment for evaluating Nix expressions:

`nix repl`

- Upgrade Nix to the latest stable version:

`nix upgrade-nix`
