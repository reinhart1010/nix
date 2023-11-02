---
layout: page
title: common/nix-build (Deutsch)
description: "Erstellen eines Nix-Ausdrucks."
content_hash: 4484623e9a108440747211b68df80d4bff41596d
last_modified_at: 2023-11-02
related_topics:
  - title: English version
    url: /en/common/nix-build.html
    icon: bi bi-globe
---
# nix-build

Erstellen eines Nix-Ausdrucks.
Weitere Informationen: <https://nixos.org/manual/nix/stable/command-ref/nix-build.html>.

- Erstelle einen Nix-Ausdruck:

`nix-build '<nixpkgs>' --attr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">firefox</span>

- Erstelle einen gesandboxten Nix-Ausdruck (auf nicht-NixOS):

`nix-build '<nixpkgs>' --attr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">firefox</span>` --option sandbox true`
