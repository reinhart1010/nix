---
layout: page
title: linux/pacman (Deutsch)
description: "Arch Linux Paket Management Tool."
content_hash: ac20ce439f22a6a76ed18515480cf119a156f4ce
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
  - title: português (Portugal) version
    url: /pt_PT/linux/pacman.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman.html
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

`sudo pacman -Syu`

- Installiere ein neues Paket:

`sudo pacman -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>

- Entferne ein Paket und dessen Abhängigkeiten:

`sudo pacman -Rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>

- Suche in der Paketdatenbank nach einem regulären Ausdruck oder Schlüsselwort:

`pacman -Ss "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">suchmuster</span>`"`

- Liste alle installierten Pakete und dessen Versionen auf:

`pacman -Q`

- Liste alle ausdrücklich installierten Pakete und dessen Versionen auf:

`pacman -Qe`

- Zeige verwaiste Pakete an, welche als Abhängigkeiten installiert wurden, aber nicht mehr von anderen Paketen benötigt werden:

`pacman -Qtdq`

- Leere den gesamten pacman Cache:

`sudo pacman -Scc`
