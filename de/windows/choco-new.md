---
layout: page
title: windows/choco-new (Deutsch)
description: "Erstelle neue Paket-Beschreibungs-Dateien mit Chocolatey."
content_hash: fa4476f719368ca217b950d0e8d6db3fa5677896
related_topics:
  - title: English version
    url: /en/windows/choco-new.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-new.html
    icon: bi bi-globe
---
# choco new

Erstelle neue Paket-Beschreibungs-Dateien mit Chocolatey.
Weitere Informationen: <https://chocolatey.org/docs/commands-new>.

- Erstelle ein neues Grundgerüst für ein Paket:

`choco new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_name</span>

- Erstelle ein neues Paket mit einer bestimmten Version:

`choco new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_name</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Erstelle ein neues Paket mit einem bestimmten Betreuer*innen-Namen:

`choco new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_name</span>` --maintainer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">betreuer*innen_name</span>

- Erstelle ein neues Paket in einem bestimmten Ausgabe-Verzeichnis:

`choco new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_name</span>` --output-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>

- Erstelle ein neues Paket mit verschiedenen URLs für die 32-Bit und 64-Bit Installationsroutinen:

`choco new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_name</span>` url="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`" url64="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`"`
