---
layout: page
title: common/nix (English)
description: "A powerful package manager that makes package management reliable, reproducible, and declarative."
content_hash: 7db688249df95ee6d07eaed56234b7060ed10f3c
last_modified_at: 2024-02-15
related_topics:
  - title: Deutsch version
    url: /de/common/nix.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nix

A powerful package manager that makes package management reliable, reproducible, and declarative.
`nix` is experimental and requires enabling experimental features. For a classic, stable interface, see `tldr nix classic`.
Some subcommands such as `build`, `develop`, `flake`, `registry`, `profile`, `search`, `repl`, `store`, `edit`, `why-depends`, etc. have their own usage documentation.
More information: <https://nixos.org/manual/nix>.

- Enable the `nix` command:

`mkdir -p ~/.config/nix; echo 'experimental-features = nix-command flakes' > ~/.config/nix/nix.conf`

- Search for a package in nixpkgs via its name or description:

`nix search nixpkgs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_term</span>

- Start a shell with the specified packages from nixpkgs available:

`nix shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nixpkgs#pkg1 nixpkgs#pkg2 nixpkgs#pkg3 ...</span>

- Install some packages from nixpkgs permanently:

`nix profile install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nixpkgs#pkg1 nixpkgs#pkg2 nixpkgs#pkg3 ...</span>

- Remove unused paths from Nix store to free up space:

`nix store gc`

- Start an interactive environment for evaluating Nix expressions:

`nix repl`

- Display help for a specific subcommand:

`nix help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>
