---
layout: page
title: common/nix3-store (English)
description: "Manipulate the Nix store."
content_hash: 1ae1b168a6437e4d503fc827a22277f7f868c74a
last_modified_at: 2023-04-26
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># nix store

Manipulate the Nix store.
See also: `tldr nix-store`.
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
