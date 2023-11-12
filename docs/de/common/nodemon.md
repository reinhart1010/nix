---
layout: page
title: common/nodemon (Deutsch)
description: "Beobachtet Dateien und startet Node Applikationen automatisch neu, wenn Änderungen erkannt wurden."
content_hash: dce6a8d7fb6692c34f6aafbd63c0730595a18a96
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/nodemon.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nodemon

Beobachtet Dateien und startet Node Applikationen automatisch neu, wenn Änderungen erkannt wurden.
Weitere Informationen: <https://nodemon.io>.

- Führe die angegebene Datei aus und warte auf Änderungen:

`nodemon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.js</span>

- Manueller Neustart von Nodemon (beachte, dass Nodemon dabei aktiv sein muss):

`rs`

- Ignoriere bestimmte Dateien:

`nodemon --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei_oder_verzeichnis</span>

- Übergib Argumente an die Node Applikation:

`nodemon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.js</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumente</span>

- Übergib Argumente an node selbst, wenn sie nicht bereits Argumente von nodemon sind (z.B. `--inspect`):

`nodemon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumente</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.js</span>

- Führe Nicht-Node Skripte aus:

`nodemon --exec "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl_um_skript_auszuführen</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumente</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/skript</span>

- Führe ein Python-Skript aus:

`nodemon --exec "python `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumente</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.py</span>
