---
layout: page
title: common/nix-collect-garbage (English)
description: "Delete unused and unreachable nix store paths."
content_hash: c82e71e01aabfdeb8ec8635645a1a022d344b945
last_modified_at: 2022-12-22
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

`sudo nix-collect-garbage --delete-older-than 30d`
