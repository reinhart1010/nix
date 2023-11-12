---
layout: page
title: linux/apt-cache (Deutsch)
description: "Debian und Ubuntu-Paketsuche."
content_hash: cd83cab70c6b1be3b0a5258c75da14219d50f650
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/apt-cache.html
    icon: bi bi-globe
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
  - title: polski version
    url: /pl/linux/apt-cache.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-cache.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/apt-cache.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-cache.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-cache

Debian und Ubuntu-Paketsuche.
Weitere Informationen: <https://manpages.debian.org/latest/apt/apt-cache.8.html>.

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
