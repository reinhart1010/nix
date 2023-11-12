---
layout: page
title: linux/yay (Deutsch)
description: "Yet Another Yogurt: Ein Programm für Arch Linux um Pakete vom Arch User Repository zu installieren."
content_hash: 0f2bd5493253c439f1d96d1e831608aafa93bfd4
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/yay.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/yay.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/yay.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/yay.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yay

Yet Another Yogurt: Ein Programm für Arch Linux um Pakete vom Arch User Repository zu installieren.
Siehe auch `pacman`.
Weitere Informationen: <https://github.com/Jguer/yay>.

- Suche und installiere Pakete von den Repositorys und dem AUR interaktiv:

`yay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname|suchbegriff</span>

- Synchronisiere und aktualisiere alle Pakete von den Repositorys und dem AUR:

`yay`

- Synchronisiere und aktualisiere nur AUR-Pakete:

`yay -Sua`

- Installiere ein neues Paket von den Repositorys und dem AUR:

`yay -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>

- Entferne ein Paket sowie alle Abhängigkeiten und Konfigurationsdateien:

`yay -Rns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>

- Suche in der Paketdatenbank nach einem Schlüsselwort in den Repositorys und dem AUR:

`yay -Ss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">schlüsselwort</span>

- Entferne verwaiste Pakete (als Abhängigkeit installiert, aber von keinem Paket benötigt):

`yay -Yc`

- Zeige Statistiken für installierte Pakete sowie die Gesundheit des Systems an:

`yay -Ps`
