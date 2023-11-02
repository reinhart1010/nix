---
layout: page
title: common/nix (Deutsch)
description: "Dienstprogramme für die Nix-Sprache und den Nix-Speicher."
content_hash: 524097b5a027c9e2231db754208c3de35a8590d8
last_modified_at: 2023-11-02
related_topics:
  - title: English version
    url: /en/common/nix.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nix.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

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
