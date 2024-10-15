---
layout: page
title: common/nix3-develop (English)
description: "Run a Bash shell that provides the build environment of a derivation."
content_hash: 00591bfa14ff6fa542c02043d46e28dd3fde52b3
last_modified_at: 2024-10-15
tldri18n_status: 2
---
# nix develop

Run a Bash shell that provides the build environment of a derivation.
More information: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-develop.html>.

- Start a shell with all dependencies of a package from nixpkgs available:

`nix develop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nixpkgs#pkg</span>

- Start a development shell for the default package in a flake in the current directory:

`nix develop`

- In that shell, configure and build the sources:

`configurePhase; buildPhase`
