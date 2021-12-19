---
layout: page
title: linux/pacman-remove (Deutsch)
description: "Arch Linux Paketverwaltungs-Werkzeug."
content_hash: 664380dd5f7d620db7b0af2134e6912c82edfb1b
related_topics:
  - title: English version
    url: /en/linux/pacman-remove.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-remove.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman-remove.html
    icon: bi bi-globe
---
# pacman --remove

Arch Linux Paketverwaltungs-Werkzeug.
Weitere Informationen: <https://man.archlinux.org/man/pacman.8>.

- Zeige Hilfe für diesen Unterbefehl an:

`pacman --remove --help`

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
