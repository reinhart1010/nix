---
layout: page
title: common/nix-build (English)
description: "Build a Nix expression."
content_hash: 764b8de463d9e5af9666fec16f26343f58a4a6d0
---
# nix-build

Build a Nix expression.
More information: <https://nixos.org/releases/nix/latest/manual#sec-nix-build>.

- Build a Nix expression:

`nix-build --attr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression_name</span>

- Build a sandboxed Nix expression (on non-NixOS):

`nix-build --attr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression_name</span>` --option sandbox true`
