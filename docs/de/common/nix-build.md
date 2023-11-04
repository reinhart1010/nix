---
layout: page
title: common/nix-build (Deutsch)
description: "Erstellen eines Nix-Ausdrucks."
content_hash: a83d7767a7294db0664ebf7b43d0b05831eb4b9f
last_modified_at: 2023-11-04
related_topics:
  - title: English version
    url: /en/common/nix-build.html
    icon: bi bi-globe
---
# nix-build

Erstellen eines Nix-Ausdrucks.
Weitere Informationen: <https://nixos.org/releases/nix/latest/manual#sec-nix-build>.

- Erstelle einen Nix-Ausdruck:

`nix-build '<nixpkgs>' --attr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">firefox</span>

- Erstelle einen gesandboxten Nix-Ausdruck (auf nicht-NixOS):

`nix-build '<nixpkgs>' --attr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">firefox</span>` --option sandbox true`
