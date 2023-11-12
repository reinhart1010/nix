---
layout: page
title: common/borg (Deutsch)
description: "Deduplizierendes Sicherungswerkzeug."
content_hash: 2345f58d391f716be7bb9f560294280bd6f66c68
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/borg.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/borg.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/borg.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/borg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# borg

Deduplizierendes Sicherungswerkzeug.
Erstellt lokale oder entfernte Sicherungen, die als Dateisysteme einhängbar sind.
Weitere Informationen: <https://borgbackup.readthedocs.io/en/stable/usage/general.html>.

- Initialisiere ein lokales Repository:

`borg init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/repo_verzeichnis</span>

- Sichere ein Verzeichnis in das Repository und erstelle ein Archiv mit dem Namen "Montag":

`borg create --progress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/repo_verzeichnis</span>`::`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Montag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/quell_verzeichnis</span>

- Liste alle Archive in einem Repository auf:

`borg list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/repo_verzeichnis</span>

- Extrahiere ein bestimmtes Verzeichnis aus dem "Montag"-Archiv in einem entfernten Repository, unter Ausschluss aller `*.ext`-Dateien:

`borg extract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzer</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/repo_verzeichnis</span>`::`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Montag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/ziel_verzeichnis} --exclude '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>`'`

- Bereinige ein Repository, indem alle Archive gelöscht werden, die älter als 7 Tage sind und Änderungen aufweisen:

`borg prune --keep-within `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7d</span>` --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/repo_verzeichnis</span>

- Hänge ein Repository als FUSE-Dateisystem ein:

`borg mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/repo_verzeichnis</span>`::`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Montag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/mountpoint</span>

- Zeige Hilfe zur Erstellung von Archiven an:

`borg create --help`
