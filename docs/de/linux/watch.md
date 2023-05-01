---
layout: page
title: linux/watch (Deutsch)
description: "Führe einen Befehl wiederholt aus und überwache die Ausgabe im Vollbildmodus."
content_hash: 73ee8ada7b6b84423a2b4c3f1b8197ce2efb38a3
last_modified_at: 2023-05-01
related_topics:
  - title: English version
    url: /en/linux/watch.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/watch.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/watch.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># watch

Führe einen Befehl wiederholt aus und überwache die Ausgabe im Vollbildmodus.
Weitere Informationen: <https://manned.org/watch>.

- Überwache die Dateien im aktuellen Verzeichnis:

`watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls</span>

- Überwache verfügbaren Festplatten-Speicherplatz und hebe die Änderungen hervor:

`watch -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">df</span>

- Überwache "node"-Prozesse und aktualisiere alle 3 Sekunden:

`watch -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ps aux | grep node</span>`"`

- Überwache, ob sich der Festplatten-Speicherplatz ändert und höre mit der Überwachung auf, sobald eine Änderung auftritt:

`watch -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">df</span>
