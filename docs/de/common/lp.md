---
layout: page
title: common/lp (Deutsch)
description: "Druckt Dateien."
content_hash: 25152c8ddc9b84fc7d841f7cad25f2b45448ffc4
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/lp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lp

Druckt Dateien.
Weitere Informationen: <https://manned.org/lp>.

- Drucke die Ausgabe eines Befehls mit dem Standard-Drucker (siehe `lpstat`):

`echo "test" | lp`

- Drucke eine Datei mit dem Standard-Drucker:

`lp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Drucke eine Datei mit einem bestimmten Drucker (siehe `lpstat`):

`lp -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">druckername</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Drucke N Kopien einer Datei mit dem Standarddrucker (wobei N die Anzahl gewünschter Kopien ist):

`lp -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Drucke nur bestimmte Seiten mit dem Standarddrucker (drucke Seiten 1, 3-5 und 16):

`lp -P 1,3-5,16 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Führe einen aufgehaltenen Druckauftrag durch:

`lp -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id</span>` -H resume`
