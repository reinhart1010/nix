---
layout: page
title: common/nix-collect-garbage (Deutsch)
description: "Löschen von unbenutzten und unerreichbaren Nix-Speicherpfaden."
content_hash: 2b1b868a52613031f1505dd41ab6d989cdd0e25e
last_modified_at: 2023-01-01
related_topics:
  - title: English version
    url: /en/common/nix-collect-garbage.html
    icon: bi bi-globe
---
# nix-collect-garbage

Löschen von unbenutzten und unerreichbaren Nix-Speicherpfaden.
Generationen können mit `nix-env --list-generations` aufgelistet werden.
Weitere Informationen: <https://nixos.org/releases/nix/latest/manual/#sec-nix-collect-garbage>.

- Lösche alle Speicherpfade, die von den aktuellen Generationen der einzelnen Profile nicht verwendet werden:

`sudo nix-collect-garbage --delete-old`

- Simuliere die Löschung alter Speicherpfade:

`sudo nix-collect-garbage --delete-old --dry-run`

- Lösche alle Speicherpfade, die älter als 30 Tage sind:

`sudo nix-collect-garbage --delete-older-than 30d`
