---
layout: page
title: common/nix3-flake (English)
description: "Manage Nix flakes."
content_hash: d0b40b35956c6f139180f5f834d54a23a85b1f57
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# nix flake

Manage Nix flakes.
More information: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-flake.html>.

- Create a new flake (just the `flake.nix` file) from the default template, in the current directory:

`nix flake init`

- Update all inputs (dependencies) of the flake in the current directory:

`nix flake update`

- Update a specific input (dependency) of the flake in the current directory:

`nix flake lock --update-input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input</span>

- Show all the outputs of a flake on github:

`nix flake show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">github:owner/repo</span>

- Display help:

`nix flake --help`
