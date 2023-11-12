---
layout: page
title: common/nix-store (English)
description: "Manipulate or query the Nix store."
content_hash: 90cb13f0a82e395986f784eb5148422491c942ed
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# nix-store

Manipulate or query the Nix store.
See also: `tldr nix3 store`.
More information: <https://nixos.org/manual/nix/stable/command-ref/nix-store.html>.

- Collect garbage, such as removing unused paths:

`nix-store --gc`

- Hard-link identical files together to reduce space usage:

`nix-store --optimise`

- Delete a specific store path (must be unused):

`nix-store --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/nix/store/...</span>

- Show all dependencies of a store path (package), in a tree format:

`nix-store --query --tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/nix/store/...</span>

- Calculate the total size of a certain store path with all the dependencies:

`du -cLsh $(nix-store --query --references `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/nix/store/...</span>`)`

- Show all dependents of a particular store path:

`nix-store --query --referrers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/nix/store/...</span>
