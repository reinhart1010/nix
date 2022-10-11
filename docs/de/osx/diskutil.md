---
layout: page
title: osx/diskutil (Deutsch)
description: "Dienstprogramm zur Verwaltung lokaler Festplatten und Volumes."
content_hash: 20edd50238f88109611f5b91497ec70f281ad10f
related_topics:
  - title: English version
    url: /en/osx/diskutil.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/diskutil.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/diskutil.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/diskutil.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># diskutil

Dienstprogramm zur Verwaltung lokaler Festplatten und Volumes.
Weitere Informationen: <https://ss64.com/osx/diskutil.html>.

- Auflisten aller aktuell verfügbaren Festplatten, Partitionen und gemounteten Volumes:

`diskutil list`

- Reparieren der Dateisystem-Datenstrukturen eines Volumes:

`diskutil repairVolume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/diskX</span>

- Einen Datenträger aushängen:

`diskutil unmountDisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/diskX</span>

- Eine CD/DVD auswerfen (zuerst aushängen):

`diskutil eject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/disk1</span>
