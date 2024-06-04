---
layout: page
title: common/nix3-store (English)
description: "Manipulate the Nix store."
content_hash: 6b89daead8f5b33e865120690222119fa5975683
last_modified_at: 2024-06-04
tldri18n_status: 2
---
# nix store

Manipulate the Nix store.
See also: `nix-store`.
More information: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-store.html>.

- Collect garbage, i.e. remove unused paths to reduce space usage:

`nix store gc`

- Hard-link identical files together to reduce space usage:

`nix store optimise`

- Delete a specific store path (most be unused):

`nix store delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/nix/store/...</span>

- List a contents of the store path, on a remote store:

`nix store --store `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://cache.nixos.org</span>` ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/nix/store/...</span>

- Show the differences in versions between two store paths, with their respective dependencies:

`nix store diff-closures `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/nix/store/...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/nix/store/...</span>
