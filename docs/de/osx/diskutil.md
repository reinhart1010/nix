---
layout: page
title: osx/diskutil (Deutsch)
description: "Dienstprogramm zur Verwaltung lokaler Festplatten und Volumes."
content_hash: 77a4e1b812470b2d633f0d6a0c4232d014bdc1f2
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/diskutil.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/diskutil.html
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
tldri18n_status: 2
---
# diskutil

Dienstprogramm zur Verwaltung lokaler Festplatten und Volumes.
Weitere Informationen: <https://keith.github.io/xcode-man-pages/diskutil.8.html>.

- Auflisten aller aktuell verfügbaren Festplatten, Partitionen und gemounteten Volumes:

`diskutil list`

- Reparieren der Dateisystem-Datenstrukturen eines Volumes:

`diskutil repairVolume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/diskX</span>

- Einen Datenträger aushängen:

`diskutil unmountDisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/diskX</span>

- Eine CD/DVD auswerfen (zuerst aushängen):

`diskutil eject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/disk1</span>
