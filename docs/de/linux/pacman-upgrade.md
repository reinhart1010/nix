---
layout: page
title: linux/pacman-upgrade (Deutsch)
description: "Arch Linux Paketverwaltungs-Werkzeug."
content_hash: 5765c4ff247370eb3c429c1e1e40dfb60c1920b1
last_modified_at: 2024-09-25
related_topics:
  - title: English version
    url: /en/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-upgrade.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --upgrade

Arch Linux Paketverwaltungs-Werkzeug.
Siehe auch: `pacman`.
Weitere Informationen: <https://manned.org/pacman.8>.

- Installiere ein oder mehrere Pakete von Dateien:

`sudo pacman --upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/paket1.pkg.tar.zst</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/paket2.pkg.tar.zst</span>

- Installiere ein Paket ohne Bestätigungsaufforderung:

`sudo pacman --upgrade --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/paket.pkg.tar.zst</span>

- Überschreibe widersprüchliche Dateien während einer Paketinstallation:

`sudo pacman --upgrade --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/paket.pkg.tar.zst</span>

- Installiere ein Paket und überspringe die Überprüfung von Abhängigkeitsversionen:

`sudo pacman --upgrade --nodeps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/paket.pkg.tar.zst</span>

- Liste Pakete auf, welche betroffen sein würden (installiert keine Pakete):

`pacman --upgrade --print `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/paket.pkg.tar.zst</span>

- Zeige Hilfe an:

`pacman --upgrade --help`
