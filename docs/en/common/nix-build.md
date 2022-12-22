---
layout: page
title: common/nix-build (English)
description: "Build a Nix expression."
content_hash: 8adc459844860b2e362208b59e8fe8a48930d60e
last_modified_at: 2022-12-22
---
# nix-build

Build a Nix expression.
More information: <https://nixos.org/releases/nix/latest/manual#sec-nix-build>.

- Build a Nix expression:

`nix-build '<nixpkgs>' --attr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">firefox</span>

- Build a sandboxed Nix expression (on non-NixOS):

`nix-build '<nixpkgs>' --attr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">firefox</span>` --option sandbox true`
