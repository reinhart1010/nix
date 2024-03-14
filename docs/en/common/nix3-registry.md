---
layout: page
title: common/nix3-registry (English)
description: "Manage a Nix flake registry."
content_hash: bcb5a744d84c47c0e8a5474957a68abc0304d640
last_modified_at: 2024-03-14
tldri18n_status: 2
---
# nix registry

Manage a Nix flake registry.
See `tldr nix3 flake` for information about flakes.
More information: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-registry.html>.

- Pin the `nixpkgs` revision to the current version of the upstream repository:

`nix registry pin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nixpkgs</span>

- Pin an entry to the latest version of the branch, or a particular reivision of a GitHub repository:

`nix registry pin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">entry</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">github:owner/repo/branch_or_revision</span>

- Add a new entry that always points to the latest version of a GitHub repository, updating automatically:

`nix registry add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">entry</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">github:owner/repo</span>

- Remove a registry entry:

`nix registry remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">entry</span>

- See documentation about what Nix flake registries are:

`nix registry --help`
