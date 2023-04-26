---
layout: page
title: common/nix-build (English)
description: "Build a Nix expression."
content_hash: 3af4a335315e6679f7f63fbf62199e4e57b1efc6
last_modified_at: 2023-04-26
related_topics:
  - title: Deutsch version
    url: /de/common/nix-build.html
    icon: bi bi-globe
---
# nix-build

Build a Nix expression.
See also: `tldr nix3 build`.
More information: <https://nixos.org/manual/nix/stable/command-ref/nix-build.html>.

- Build a Nix expression:

`nix-build '<nixpkgs>' --attr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">firefox</span>

- Build a sandboxed Nix expression (on non-NixOS):

`nix-build '<nixpkgs>' --attr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">firefox</span>` --option sandbox true`
