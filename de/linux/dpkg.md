---
layout: page
title: linux/dpkg (Deutsch)
description: "Debian Paketmanager."
content_hash: a75ce0a6ef9d9bd93d524130f857b15fe188da40
related_topics:
  - title: English version
    url: /en/linux/dpkg.html
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
Weitere Informationen: <https://manpages.debian.org/buster/dpkg/dpkg.1.en.html>.

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
