---
layout: page
title: common/nix3-search (English)
description: "Search for packages in a Nix flake."
content_hash: cf0e78fa875b470b9a74b5bf7ac383aa6e5ac3cc
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# nix search

Search for packages in a Nix flake.
See `tldr nix3 flake` for information about flakes.
More information: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-search.html>.

- Search `nixpkgs` for a package based on its name or description:

`nix search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nixpkgs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_term...</span>

- Show description of a package from nixpkgs:

`nix search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nixpkgs#pkg</span>

- Show all packages available from a flake on github:

`nix search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">github:owner/repo</span>
