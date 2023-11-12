---
layout: page
title: linux/paru (Deutsch)
description: "Ein AUR-Helfer und pacman-Wrapper."
content_hash: cc14cc50e388f9b746fc37b22c431f63beef3396
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/paru.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/paru.html
    icon: bi bi-globe
tldri18n_status: 2
---
# paru

Ein AUR-Helfer und pacman-Wrapper.
Weitere Informationen: <https://github.com/Morganamilo/paru>.

- Interaktiv nach einem Paket suchen und es installieren:

`paru `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname_oder_suchbegriff</span>

- Alle Pakete synchronisieren und aktualisieren:

`paru`

- AUR-Pakete aktualisieren:

`paru -Sua`

- Informationen über ein Paket abrufen:

`paru -Si `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>

- Herunterladen von `PKGBUILD` und anderen Paket-Quelldateien aus dem AUR oder dem ABS:

`paru --getpkgbuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>

- Anzeigen der `PKGBUILD`-Datei eines Pakets:

`paru --getpkgbuild --print `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>
