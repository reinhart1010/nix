---
layout: page
title: linux/pacman-remove (Deutsch)
description: "Arch Linux Paketverwaltungs-Werkzeug."
content_hash: e4f619b93f2c9cf4aca30d2a81d35373e0949c7c
last_modified_at: 2024-09-25
related_topics:
  - title: English version
    url: /en/linux/pacman-remove.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-remove.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/pacman-remove.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman-remove.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-remove.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-remove.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman-remove.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --remove

Arch Linux Paketverwaltungs-Werkzeug.
Siehe auch: `pacman`.
Weitere Informationen: <https://manned.org/pacman.8>.

- Entferne ein Paket und dessen Abhängigkeiten:

`sudo pacman --remove --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>

- Entferne ein Paket sowie alle Abhängigkeiten und Konfigurationsdateien:

`sudo pacman --remove --recursive --nosave `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>

- Entferne ein Paket ohne Bestätigungsaufforderung:

`sudo pacman --remove --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>

- Entferne verwaiste Pakete (Pakete welche als Abhängigkeit installiert wurden, aber von keinem Paket benötigt werden):

`sudo pacman --remove --recursive --nosave $(pacman --query --unrequired --deps --quiet)`

- Entferne ein Paket und alle Pakete die davon abhängig sind:

`sudo pacman --remove --cascade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>

- Liste Pakete auf, welche betroffen sein würden (entfernt keine Pakete):

`pacman --remove --print `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>

- Zeige Hilfe für diesen Unterbefehl an:

`pacman --remove --help`
