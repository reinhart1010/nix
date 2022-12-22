---
layout: page
title: common/nix (Deutsch)
description: "Dienstprogramme für die Nix-Sprache und den Nix-Speicher."
content_hash: b7017282a8e7250f6312b405edbeab9fb54b4cc7
last_modified_at: 2022-12-22
related_topics:
  - title: English version
    url: /en/common/nix.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># nix

Dienstprogramme für die Nix-Sprache und den Nix-Speicher.
Weitere Informationen: <https://nixos.org>.

- Suche nach einem Paket über seinen Namen oder seine Beschreibung:

`nix search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">suchbegriff</span>

- Starten einer Nix-Shell, die die angegebenen Pakete zur Verfügung stellt:

`nix run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nixpkgs.pkg1 nixpkgs.pkg2 ...</span>

- Optimieren der Festplattennutzung des Nix-Speicher durch Zusammenfassen doppelter Dateien:

`nix store optimise`

- Starten einer interaktiven Umgebung für die Auswertung von Nix-Ausdrücken:

`nix repl`

- Upgrade von Nix auf die neueste stabile Version:

`nix upgrade-nix`
