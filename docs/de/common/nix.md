---
layout: page
title: common/nix (Deutsch)
description: "Dienstprogramme für die Nix-Sprache und den Nix-Speicher."
content_hash: 524097b5a027c9e2231db754208c3de35a8590d8
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/nix.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># nix

Dienstprogramme für die Nix-Sprache und den Nix-Speicher.
Weitere Informationen: <https://nixos.org/manual/nix>.

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
