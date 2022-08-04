---
layout: page
title: linux/apt-get (Deutsch)
description: "Debian und Ubuntu Paket Management Tool."
content_hash: 27d1bded6825590d760b77f354e5b43f4bf3b234
related_topics:
  - title: English version
    url: /en/linux/apt-get.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-get.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt-get.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-get.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-get.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/apt-get.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-get.html
    icon: bi bi-globe
---
# apt-get

Debian und Ubuntu Paket Management Tool.
Suche mit `apt-cache` nach Paketen.
Weitere Informationen: <https://manpages.debian.org/latest/apt/apt-get.8.html>.

- Aktualisiere die Liste der Paketquellen (es wird empfohlen diesen Befehl zu Beginn auszuführen):

`apt-get update`

- Installiere ein Paket oder aktualisiere es zur neuesten Version:

`apt-get install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Entferne ein Paket:

`apt-get remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Entferne ein Paket und die dazugehörigen Konfigurationen:

`apt-get purge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Aktualisiere alle Pakete auf die neueste Version:

`apt-get upgrade`

- Reinige das Repository

`apt-get autoclean`

- Entferne alle Pakete, die nicht mehr benötigt werden:

`apt-get autoremove`

- Aktualisiere alle Pakete (wie `upgrade`), aber entfernt alle obsoleten Pakete:

`apt-get dist-upgrade`
