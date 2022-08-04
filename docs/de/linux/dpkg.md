---
layout: page
title: linux/dpkg (Deutsch)
description: "Debian Paketmanager."
content_hash: 24021ea175d7b237e76dccb892bfd7eebdc98021
related_topics:
  - title: English version
    url: /en/linux/dpkg.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/dpkg.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/dpkg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dpkg.html
    icon: bi bi-globe
---
# dpkg

Debian Paketmanager.
Manche Unterbefehle wie `dpkg deb` sind separat dokumentiert.
Weitere Informationen: <https://manpages.debian.org/latest/dpkg/dpkg.html>.

- Installiere ein Paket:

`dpkg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.deb</span>

- Entferne ein Paket:

`dpkg -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>

- Liste installierte Pakete auf:

`dpkg -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">muster</span>

- Liste die Inhalte eines Pakets auf:

`dpkg -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>

- Liste die Inhalte einer lokalen Paketdatei auf:

`dpkg -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.deb</span>

- Finde heraus welche Pakete eine Datei besitzen:

`dpkg -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dateiname</span>
