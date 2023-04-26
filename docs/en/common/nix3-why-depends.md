---
layout: page
title: common/nix3-why-depends (English)
description: "Show why a package depends on another package."
content_hash: fba82b8d2bdfa25d2190d74b5abf632f89420b05
last_modified_at: 2023-04-26
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># nix why-depends

Show why a package depends on another package.
More information: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-why-depends.html>.

- Show why the currently running NixOS system requires a certain store path:

`nix why-depends `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/run/current-system</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/nix/store/...</span>

- Show why a package from nixpkgs requires another package as a _build-time_ dependency:

`nix why-depends --derivation `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nixpkgs#dependent</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nixpkgs#dependency</span>
