---
layout: page
title: common/nix-collect-garbage (English)
description: "Delete unused and unreachable nix store paths."
content_hash: f54b8ef128a600dbc00cd0fc50b5b37b0f3cf605
---
# nix-collect-garbage

Delete unused and unreachable nix store paths.
Generations can be listed using `nix-env --list-generations`.
More information: <https://nixos.org/releases/nix/latest/manual/#sec-nix-collect-garbage>.

- Delete all store paths unused by current generations of each profile:

`sudo nix-collect-garbage --delete-old`

- Simulate the deletion of old store paths:

`sudo nix-collect-garbage --delete-old --dry-run`

- Delete all store paths older than 30 days:

`sudo nix-collect-garbage --delete-older-than `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30d</span>
