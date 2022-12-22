---
layout: page
title: common/nix-collect-garbage (Deutsch)
description: "Löschen von unbenutzten und unerreichbaren Nix-Speicherpfaden."
content_hash: a2ee2af0258c145d5b16edfbdf233bd43325fa66
last_modified_at: 2022-12-22
related_topics:
  - title: English version
    url: /en/common/nix-collect-garbage.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># nix-collect-garbage

Löschen von unbenutzten und unerreichbaren Nix-Speicherpfaden.
Generationen können mit `nix-env --list-generations` aufgelistet werden.
Weitere Informationen: <https://nixos.org/releases/nix/latest/manual/#sec-nix-collect-garbage>.

- Löschen von allen Speicherpfaden, die von den aktuellen Generationen der einzelnen Profile nicht verwendet werden:

`sudo nix-collect-garbage --delete-old`

- Simulieren der Löschung alter Speicherpfade:

`sudo nix-collect-garbage --delete-old --dry-run`

- Löschen aller Speicherpfade, die älter als 30 Tage sind:

`sudo nix-collect-garbage --delete-older-than 30d`
