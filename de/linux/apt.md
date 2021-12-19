---
layout: page
title: linux/apt (Deutsch)
description: "Debian und Ubuntu Paket Management Tool."
content_hash: 1d26c01868ce65f6ef56bdfc2dab6aed86fdc53d
related_topics:
  - title: বাংলা version
    url: /bn/linux/apt.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/apt.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/apt.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/apt.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt.html
    icon: bi bi-globe
---
# apt

Debian und Ubuntu Paket Management Tool.
Empfohlene Alternative zu apt-get seit Ubuntu 16.04.
Weitere Informationen: <https://manpages.debian.org/latest/apt/apt.8.html>.

- Aktualisiere die Liste der Paketquellen (es wird empfohlen, diesen Befehl zu Beginn auszuführen):

`sudo apt update`

- Suche nach einem Paket:

`apt search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Zeige Informationen über ein Paket:

`apt show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Installiere ein Paket oder aktualisiere es zur neusten Version:

`sudo apt install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Entferne ein Paket:

`sudo apt remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Aktualisiere alle installierten Pakete auf die neueste Version:

`sudo apt upgrade`

- Liste alle Pakete auf:

`apt list`

- Liste alle installierten Pakete auf:

`apt list --installed`
