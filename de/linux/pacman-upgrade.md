---
layout: page
title: linux/pacman-upgrade (Deutsch)
description: "Arch Linux Paketverwaltungs-Werkzeug."
content_hash: aacf96ec299301885488a0af9596fcd61d963c0f
related_topics:
  - title: English version
    url: /en/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-upgrade.html
    icon: bi bi-globe
---
# pacman --upgrade

Arch Linux Paketverwaltungs-Werkzeug.
Weitere Informationen: <https://man.archlinux.org/man/pacman.8>.

- Zeige Hilfe an:

`pacman --upgrade --help`

- Installiere ein oder mehrere Pakete von Dateien:

`sudo pacman --upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/paket1.pkg.tar.zst</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/paket2.pkg.tar.zst</span>

- Installiere ein Paket ohne Bestätigungsaufforderung:

`sudo pacman --upgrade --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/paket.pkg.tar.zst</span>

- Überschreibe widersprüchliche Dateien während einer Paketinstallation:

`sudo pacman --upgrade --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/paket.pkg.tar.zst</span>

- Installiere ein Paket und überspringe die Überprüfung von Abhängigkeitsversionen:

`sudo pacman --upgrade --nodeps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/paket.pkg.tar.zst</span>

- Liste Pakete auf, welche betroffen sein würden (installiert keine Pakete):

`pacman --query --print `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/paket.pkg.tar.zst</span>
