---
layout: page
title: linux/pacman (Deutsch)
description: "Arch Linux Paket Management Tool."
content_hash: a6cef858d8820dfd41e5377d3850f0ee56248dae
related_topics:
  - title: English version
    url: /en/linux/pacman.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/pacman.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pacman.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/pacman.html
    icon: bi bi-globe
---
# pacman

Arch Linux Paket Management Tool.
Manche Unterbefehle wie `pacman sync` sind separat dokumentiert.
Weitere Informationen: <https://man.archlinux.org/man/pacman.8>.

- Synchronisiere und aktualisiere alle Pakete:

`sudo pacman --sync --refresh --sysupgrade`

- Installiere ein neues Paket:

`sudo pacman --sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>

- Entferne ein Paket und dessen Abhängigkeiten:

`sudo pacman --remove --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>

- Suche in der Paketdatenbank nach einem regulären Ausdruck oder Schlüsselwort:

`pacman --sync --search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">suchmuster</span>`"`

- Liste alle installierten Pakete und dessen Versionen auf:

`pacman --query`

- Liste alle ausdrücklich installierten Pakete und dessen Versionen auf:

`pacman --query --explicit`

- Zeige verwaiste Pakete an, welche als Abhängigkeiten installiert wurden, aber nicht mehr von anderen Paketen benötigt werden.

`pacman --query --unrequired --deps --quiet`

- Leere den gesamten pacman Cache:

`sudo pacman --sync --clean --clean`
