---
layout: page
title: common/nix-collect-garbage (Deutsch)
description: "Löschen von unbenutzten und unerreichbaren Nix-Speicherpfaden."
content_hash: 15675844fcfb40fd3ed3dbed17633cb908f2cc39
last_modified_at: 2023-11-20
related_topics:
  - title: English version
    url: /en/common/nix-collect-garbage.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nix-collect-garbage

Löschen von unbenutzten und unerreichbaren Nix-Speicherpfaden.
Generationen können mit `nix-env --list-generations` aufgelistet werden.
Weitere Informationen: <https://nixos.org/manual/nix/stable/command-ref/nix-collect-garbage.html>.

- Lösche alle Speicherpfade, die von den aktuellen Generationen der einzelnen Profile nicht verwendet werden:

`sudo nix-collect-garbage --delete-old`

- Simuliere die Löschung alter Speicherpfade:

`sudo nix-collect-garbage --delete-old --dry-run`

- Lösche alle Speicherpfade, die älter als 30 Tage sind:

`sudo nix-collect-garbage --delete-older-than 30d`
