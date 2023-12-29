---
layout: page
title: common/lpr (Deutsch)
description: "CUPS-Programm zum Drucken von Dateien."
content_hash: de927a40990b124a10792347433c67c6bb997736
last_modified_at: 2023-12-29
related_topics:
  - title: English version
    url: /en/common/lpr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lpr

CUPS-Programm zum Drucken von Dateien.
Siehe auch: `lpstat` und `lpadmin`.
Weitere Informationen: <https://openprinting.github.io/cups/doc/man-lpr.html>.

- Drucke eine Datei mit dem Standarddrucker:

`lpr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Drucke 2 Kopien einer Datei:

`lpr -# `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Drucke eine Datei mit einem bestimmten Drucker:

`lpr -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">druckername</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Drucke entweder eine einzelne Seite (z. B. 2) oder mehrere Seiten (z. B. 2-16):

`lpr -o page-ranges=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2|2-16</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Drucke doppelseitig entweder gespiegelt an der langen oder an der kurzen Seite:

`lpr -o sides=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">two-sided-long-edge|two-sided-short-edge</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Drucke mit festgelegter Papiergröße (je nach Drucker-Konfiguration gibt es mehr Optionen):

`lpr -o media=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a4|letter|legal</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Drucke mehrere Seiten pro Blatt:

`lpr -o number-up=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2|4|6|9|16</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>
