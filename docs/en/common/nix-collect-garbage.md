---
layout: page
title: common/nix-collect-garbage (English)
description: "Delete unused and unreachable nix store paths."
content_hash: 73ed4c3a4a603f76be24575c770a6a8fe4e58f9c
last_modified_at: 2023-11-20
related_topics:
  - title: Deutsch version
    url: /de/common/nix-collect-garbage.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nix-collect-garbage

Delete unused and unreachable nix store paths.
Generations can be listed using `nix-env --list-generations`.
More information: <https://nixos.org/manual/nix/stable/command-ref/nix-collect-garbage.html>.

- Delete all store paths unused by current generations of each profile:

`sudo nix-collect-garbage --delete-old`

- Simulate the deletion of old store paths:

`sudo nix-collect-garbage --delete-old --dry-run`

- Delete all store paths older than 30 days:

`sudo nix-collect-garbage --delete-older-than 30d`
