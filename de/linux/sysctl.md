---
layout: page
title: linux/sysctl (Deutsch)
description: "Laufzeit-Kernelparameter auflisten und ändern."
content_hash: c7138eaa90b628a40f7b3c8087a9f634d2b40c43
related_topics:
  - title: English version
    url: /en/linux/sysctl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/sysctl.html
    icon: bi bi-globe
---
# sysctl

Laufzeit-Kernelparameter auflisten und ändern.

- Liste alle verfügbaren Kernelparameter mit ihren Werten auf:

`sysctl -a`

- Setze einen veränderbaren Kernelparameter:

`sysctl -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sektion.tunable</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wert</span>

- Frage aktuell geöffnete Datei-Handler ab:

`sysctl fs.file-nr`

- Frage die maximale Anzahl geöffneter Dateien ab:

`sysctl fs.file-max`

- Übernimm Änderungen aus der `/etc/sysctl.conf` Datei:

`sysctl -p`
