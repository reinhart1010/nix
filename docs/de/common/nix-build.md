---
layout: page
title: common/nix-build (Deutsch)
description: "Erstellen eines Nix-Ausdruck."
content_hash: 8a3cce8ba139a70c47e2ec8940d33de530882d68
last_modified_at: 2022-12-22
related_topics:
  - title: English version
    url: /en/common/nix-build.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># nix-build

Erstellen eines Nix-Ausdruck.
Weitere Informationen: <https://nixos.org/releases/nix/latest/manual#sec-nix-build>.

- Erstellen eines Nix-Ausdrucks:

`nix-build '<nixpkgs>' --attr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">firefox</span>

- Erstellen eines Nix-Ausdruck mit Sandbox (auf nicht-NixOS):

`nix-build '<nixpkgs>' --attr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">firefox</span>` --option sandbox true`
