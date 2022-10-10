---
layout: page
title: common/dd (Deutsch)
description: "Konvertiere und kopiere eine Datei."
content_hash: 3f78f8c5733f5805fa782c10f5f3656a0cab7919
related_topics:
  - title: English version
    url: /en/common/dd.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dd.html
    icon: bi bi-globe
---
# dd

Konvertiere und kopiere eine Datei.
Weitere Informationen: <https://www.gnu.org/software/coreutils/dd>.

- Erstelle ein bootbares USB-Laufwerk von einer isohybriden Datei (wie `archlinux-xxxx.iso`) und zeige den Fortschritt an:

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.iso</span>` of=/dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">laufwerk</span>` status=progress`

- Klone ein USB-Laufwerk in ein anderes in 4MiB Blöcken, ignoriere Fehler und zeige den Fortschritt an:

`dd if=/dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quell_laufwerk</span>` of=/dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ziel_laufwerk</span>` bs=4M conv=noerror status=progress`

- Erstelle eine Datei mit 100 zufälligen Bytes mithilfe des Zufall-Treibers des Kernels:

`dd if=/dev/urandom of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>` bs=100 count=1`

- Teste die Schreibgeschwindigkeit eines Laufwerks:

`dd if=/dev/zero of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/1GB_datei</span>` bs=1024 count=1000000`

- Erstelle ein System-Backup als IMG Datei und zeige den Fortschritt an:

`dd if=/dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">laufwerk</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.img</span>` status=progress`

- Stelle ein Laufwerk aus einer IMG Datei wieder her und zeige den Fortschritt an:

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.img</span>` of=/dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">laufwerk</span>` status=progress`

- Überprüfe den Fortschritt eines laufenden dd-Prozesses (Führe diesen Befehl von einer anderen Shell aus):

`kill -USR1 $(pgrep ^dd)`
