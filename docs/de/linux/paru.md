---
layout: page
title: linux/paru (Deutsch)
description: "Ein AUR-Helfer und pacman-Wrapper."
content_hash: b84eb3a1fcef78427ae0bf2d2a0d9d7155f6a889
related_topics:
  - title: English version
    url: /en/linux/paru.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/paru.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># paru

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

- Herunterladen von `PKGBUILD` und anderen Paket-Quelldateien aus dem AUR oder dem ABS

`paru --getpkgbuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>

- Anzeigen der `PKGBUILD`-Datei eines Pakets:

`paru --getpkgbuild --print `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>
