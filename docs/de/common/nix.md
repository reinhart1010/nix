---
layout: page
title: common/nix (Deutsch)
description: "Dienstprogramme für die Nix-Sprache und den Nix-Speicher."
content_hash: 0e7496e27bc1bf2925522e5a6663cfe88986e4f9
last_modified_at: 2023-01-01
related_topics:
  - title: English version
    url: /en/common/nix.html
    icon: bi bi-globe
---
# nix

Dienstprogramme für die Nix-Sprache und den Nix-Speicher.
Weitere Informationen: <https://nixos.org>.

- Suche nach einem Paket über seinen Namen oder seine Beschreibung:

`nix search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">suchbegriff</span>

- Starte eine Nix-Shell, die die angegebenen Pakete zur Verfügung stellt:

`nix run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nixpkgs.pkg1 nixpkgs.pkg2 ...</span>

- Optimiere die Festplattennutzung des Nix-Speichers durch Zusammenfassen doppelter Dateien:

`nix store optimise`

- Starte eine interaktive Umgebung zum Ausführen von Nix-Ausdrücken:

`nix repl`

- Upgrade Nix auf die neueste stabile Version:

`nix upgrade-nix`
