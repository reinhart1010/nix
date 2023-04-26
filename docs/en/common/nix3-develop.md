---
layout: page
title: common/nix3-develop (English)
description: "Run a bash shell that provides the build environment of a derivation."
content_hash: e961a29b9c74c397f28c3d8c4034b5f7161e8553
last_modified_at: 2023-04-26
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># nix develop

Run a bash shell that provides the build environment of a derivation.
More information: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-develop.html>.

- Start a shell with all dependencies of a package from nixpkgs available:

`nix develop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nixpkgs#pkg</span>

- Start a development shell for the default package in a flake in the current directory:

`nix develop`

- In that shell, configure and build the sources:

`configurePhase; buildPhase`
