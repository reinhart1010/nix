---
layout: page
title: linux/pacman-files (Deutsch)
description: "Arch Linux Paketverwaltungs-Werkzeug."
content_hash: b4f26b75853550fc736f391fac563571a64a382c
last_modified_at: 2023-05-14
related_topics:
  - title: English version
    url: /en/linux/pacman-files.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-files.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-files.html
    icon: bi bi-globe
---
# pacman --files

Arch Linux Paketverwaltungs-Werkzeug.
Siehe auch: `pacman`, `pkgfile`.
Weitere Informationen: <https://man.archlinux.org/man/pacman.8>.

- Aktualisiere die Paketdatenbank:

`sudo pacman --files --refresh`

- Finde das Paket, welches eine bestimmte Datei besitzt:

`pacman --files `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dateiname</span>

- Finde das Paket, welches eine bestimmte Datei besitzt, mittels eines regulären Ausdrucks:

`pacman --files --regex '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">suchmuster</span>`'`

- Liste nur Paketnamen auf:

`pacman --files --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dateiname</span>

- Liste die Dateien auf welche einem bestimmten Paket gehören:

`pacman --files --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>

- Zeige Hilfe an:

`pacman --files --help`
