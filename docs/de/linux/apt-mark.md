---
layout: page
title: linux/apt-mark (Deutsch)
description: "Tool um den Status eines installierten Paketes zu verändern."
content_hash: 7791c2f1f7d2cda696d49c260794916236525d78
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/apt-mark.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-mark.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-mark.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt-mark.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-mark.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt-mark.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-mark.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-mark.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-mark

Tool um den Status eines installierten Paketes zu verändern.
Weitere Informationen: <https://manpages.debian.org/latest/apt/apt-mark.8.html>.

- Markiere ein Paket als automatisch installiert:

`sudo apt-mark auto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>

- Halte ein Paket auf seiner aktuellen Version und verhindere dass es aktualisiert wird:

`sudo apt-mark hold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>

- Erlaube dass ein Paket wieder aktualisiert werden darf:

`sudo apt-mark unhold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>

- Zeige manuell installierte Pakete:

`apt-mark showmanual`

- Zeige gehaltene Pakete die nicht aktualisiert werden dürfen:

`apt-mark showhold`
