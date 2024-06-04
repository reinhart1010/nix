---
layout: page
title: common/nix-build (English)
description: "Build a Nix expression."
content_hash: 87388906d4a432ca670f4d9232a312bfd3bf9e20
last_modified_at: 2024-06-04
related_topics:
  - title: Deutsch version
    url: /de/common/nix-build.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nix-build

Build a Nix expression.
See also: `nix3 build`.
More information: <https://nixos.org/manual/nix/stable/command-ref/nix-build.html>.

- Build a Nix expression:

`nix-build '<nixpkgs>' --attr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">firefox</span>

- Build a sandboxed Nix expression (on non-NixOS):

`nix-build '<nixpkgs>' --attr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">firefox</span>` --option sandbox true`
