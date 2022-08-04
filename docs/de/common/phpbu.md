---
layout: page
title: common/phpbu (Deutsch)
description: "Ein Backup framework für PHP."
content_hash: 4090b78e1d7351a3bede4648a1d3eac8687d10d1
related_topics:
  - title: English version
    url: /en/common/phpbu.html
    icon: bi bi-globe
---
# phpbu

Ein Backup framework für PHP.
Weitere Informationen: <https://phpbu.de>.

- Führe ein Backup mit der Standard `phpbu.xml` Konfigurationsdatei aus:

`phpbu`

- Führe ein Backup mit einer bestimmten Konfigurationsdatei aus:

`phpbu --configuration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/konfiguration.xml</span>

- Führe nur die angegebenen Backups aus:

`phpbu --limit=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">backup_art</span>

- Simuliere Aktionen die ausgeführt werden würden:

`phpbu --simulate`
