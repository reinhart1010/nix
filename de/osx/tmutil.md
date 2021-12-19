---
layout: page
title: osx/tmutil (Deutsch)
description: "Dienstprogramm zum Verwalten von Time Machine-Backups. Die meisten Befehle erfordern Root-Rechte."
content_hash: 2fc1e5e8542a74a1b66a0160576701eaac7ff09e
related_topics:
  - title: English version
    url: /en/osx/tmutil.html
    icon: bi bi-globe
---
# tmutil

Dienstprogramm zum Verwalten von Time Machine-Backups. Die meisten Befehle erfordern Root-Rechte.
Weitere Informationen: <https://ss64.com/osx/tmutil.html>.

- Setze ein HFS+ Laufwerk als Backupziel:

`sudo tmutil setdestination `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/einhänge_punkt</span>

- Setze eine APF-Freigabe oder SMB-Freigabe als Backupziel:

`sudo tmutil setdestination `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">protocol://benutzer[:passwort]@host/share</span>

- Hänge das angegebene Ziel an die Liste der Backupziele an:

`sudo tmutil setdestination -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ziel</span>

- Aktiviere automatische Backups:

`sudo tmutil enable`

- Deaktiviere automatische Backups:

`sudo tmutil disable`

- Starte ein Backup im Hintergrund, falls nicht bereits eines läuft:

`sudo tmutil startbackup`

- Starte ein Backup im Vordergrund, falls nicht bereits eines läuft:

`sudo tmutil startbackup -b`

- Stoppe ein laufendes Backup:

`sudo tmutil stopbackup`
