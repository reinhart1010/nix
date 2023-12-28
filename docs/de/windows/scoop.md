---
layout: page
title: windows/scoop (Deutsch)
description: "Ein Kommandozeilenwerkzeug, um Windows-Programme (hier bezeichnet als Pakete) zu installieren."
content_hash: 0545caaafd6b1d4b0f7adf282ad6acb81492220f
last_modified_at: 2023-12-28
related_topics:
  - title: বাংলা version
    url: /bn/windows/scoop.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/scoop.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/scoop.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/scoop.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/scoop.html
    icon: bi bi-globe
tldri18n_status: 2
---
# scoop

Ein Kommandozeilenwerkzeug, um Windows-Programme (hier bezeichnet als Pakete) zu installieren.
Weitere Informationen: <https://scoop.sh>.

- Installiere ein Paket:

`scoop install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Entferne ein Paket:

`scoop uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Aktualisiere alle installierten Pakete:

`scoop update --all`

- Zeige alle installierten Pakete an:

`scoop list`

- Zeige Informationen über ein bestimmtes Paket an:

`scoop info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Suche nach einem Paket:

`scoop search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Entferne die alten Versionen aller Pakete und lösche den Download-Zwischenspeicher:

`scoop cleanup --cache --all`
