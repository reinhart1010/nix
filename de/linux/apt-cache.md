---
layout: page
title: linux/apt-cache (Deutsch)
description: "Debian und Ubuntu Paket Suche."
content_hash: 0e30664addb6782c46dbb606a1174801307fa1bb
related_topics:
  - title: English version
    url: /en/linux/apt-cache.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-cache.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt-cache.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-cache.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-cache.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-cache.html
    icon: bi bi-globe
---
# apt-cache

Debian und Ubuntu Paket Suche.
Mehr Informationen: <https://manpages.debian.org/latest/apt/apt-cache.8.html>.

- Suche nach einem Paket in deinen aktuellen Paketquellen:

`apt-cache search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">suchbegriff</span>

- Zeige die Paketinformationen zu einem Paket:

`apt-cache show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Überprüfe ob ein Paket installiert und up to date ist:

`apt-cache policy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Zeige die Abhängigkeiten eines Pakets:

`apt-cache depends `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Zeige Pakete die von einem bestimmten Paket abhängen:

`apt-cache rdepends `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>
