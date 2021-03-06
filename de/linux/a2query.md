---
layout: page
title: linux/a2query (Deutsch)
description: "Zeigt Apache Laufzeitkonfigurationen auf Debian-basierten Betriebssystemen an."
content_hash: 63b8310ef0ae0b254b6dca8c75f26d6bc6627e27
related_topics:
  - title: English version
    url: /en/linux/a2query.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/a2query.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/a2query.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/a2query.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/a2query.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/a2query.html
    icon: bi bi-globe
---
# a2query

Zeigt Apache Laufzeitkonfigurationen auf Debian-basierten Betriebssystemen an.
Weitere Informationen: <https://manpages.debian.org/latest/apache2/a2query.html>.

- Zeige aktivierte Apache Module an:

`sudo a2query -m`

- Prüfe, ob ein bestimmtes Modul installiert ist:

`sudo a2query -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modulname</span>

- Zeige aktivierte virtuelle Hosts an:

`sudo a2query -s`

- Zeige das aktuell aktivierte Multi-Processing-Modul an:

`sudo a2query -M`

- Zeige die Apache Versionsnummer an:

`sudo a2query -v`
