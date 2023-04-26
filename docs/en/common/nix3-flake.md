---
layout: page
title: common/nix3-flake (English)
description: "Manage Nix flakes."
content_hash: f1e3ee0eefd14d17a62e144478a5d5f2024699ed
last_modified_at: 2023-04-26
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># nix flake

Manage Nix flakes.
More information: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-flake.html>.

- See documentation about what Nix flakes are:

`nix flake --help`

- Create a new flake (just the `flake.nix` file) from the default template, in the current directory:

`nix flake init`

- Update all inputs (dependencies) of the flake in the current directory:

`nix flake update`

- Update a specific input (dependency) of the flake in the current directory:

`nix flake lock --update-input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input</span>

- Show all the outputs of a flake on github:

`nix flake show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">github:owner/repo</span>
