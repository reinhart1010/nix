---
layout: page
title: linux/apt-get (Deutsch)
description: "Debian und Ubuntu Paket Management Tool."
content_hash: 0bc437491e69480a192fac8aa5f74ab2667c29c4
last_modified_at: 2024-09-18
related_topics:
  - title: العربية version
    url: /ar/linux/apt-get.html
    icon: bi bi-globe
  - title: català version
    url: /ca/linux/apt-get.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-get.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-get.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/apt-get.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt-get.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/apt-get.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-get.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/apt-get.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt-get.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-get.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/apt-get.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/apt-get.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-get.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-get

Debian und Ubuntu Paket Management Tool.
Suche mit `apt-cache` nach Paketen.
Weitere Informationen: <https://manned.org/apt-get.8>.

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

- Reinige das Repository:

`apt-get autoclean`

- Entferne alle Pakete, die nicht mehr benötigt werden:

`apt-get autoremove`

- Aktualisiere alle Pakete (wie `upgrade`), aber entfernt alle obsoleten Pakete:

`apt-get dist-upgrade`
