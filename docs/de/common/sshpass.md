---
layout: page
title: common/sshpass (Deutsch)
description: "Stelle SSH Passwörtern bereit."
content_hash: e9e67d686b9d2002c47b0655d082843e638723a9
related_topics:
  - title: English version
    url: /en/common/sshpass.html
    icon: bi bi-globe
---
# sshpass

Stelle SSH Passwörtern bereit.
Weitere Informationen: <https://manned.org/sshpass>.

- Stelle eine Verbindung zu einem externen Server über ein Passwort aus einem Datei-Objekt her (in diesem Fall stdin):

`sshpass -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzer</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>

- Stelle eine Verbindung zu einem externen Server mit Hilfe eines Passworts bei automatischer Akzeptierung von unbekannten SSH Schlüsseln her:

`sshpass -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">passwort</span>` ssh -o StrictHostKeyChecking=no `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzer</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>

- Stelle eine Verbindung zu einem externen Server mit Hilfe eines Passworts aus der ersten Zeile einer Datei bei automatischer Akzeptierung von unbekannten SSH Schlüsseln mit anschließender Ausführung eines Befehls her:

`sshpass -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>` ssh -o StrictHostKeyChecking=no `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzer</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>`"`
