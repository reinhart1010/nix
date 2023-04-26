---
layout: page
title: common/nix-classic (English)
description: "A classic, stable interface to a powerful package manager that makes package management reliable, reproducible, and declarative."
content_hash: 185369b20b4b63c0cc3e40b1e490cb51d72ada8b
last_modified_at: 2023-04-26
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># Nix classic interface

A classic, stable interface to a powerful package manager that makes package management reliable, reproducible, and declarative.
Some Nix commands such as `nix-build`, `nix-shell`, `nix-env`, and `nix-store` have their own pages. See also: `tldr nix`.
More information: <https://nixos.org>.

- Search for a package in nixpkgs via its name:

`nix-env -qaP `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_term_regexp</span>

- Start a shell with the specified packages available:

`nix-shell -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pkg1 pkg2 pkg3...</span>

- Install some packages permanently:

`nix-env -iA `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nixpkgs.pkg1 nixpkgs.pkg2...</span>

- Show all dependencies of a store path (package), in a tree format:

`nix-store --query --tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/nix/store/...</span>

- Update the channels (repositories):

`nix-channel --update`

- Remove unused paths from Nix store:

`nix-collect-garbage`
