---
layout: page
title: linux/watch (Deutsch)
description: "Führe einen Befehl wiederholt aus und überwache die Ausgabe im Vollbildmodus."
content_hash: f8da943983cd15b98758e9f5b5265824a3f2b84c
related_topics:
  - title: English version
    url: /en/linux/watch.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/watch.html
    icon: bi bi-globe
---
# watch

Führe einen Befehl wiederholt aus und überwache die Ausgabe im Vollbildmodus.
Weitere Informationen: <https://manned.org/watch>.

- Überwache die Dateien im aktuellen Verzeichnis:

`watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls</span>

- Überwache verfügbaren Festplatten-Speicherplatz und hebe die Änderungen hervor:

`watch -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">df</span>

- Überwache "node"-Prozesse und aktualisiere alle 3 Sekunden:

`watch -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ps aux | grep node</span>`"`
