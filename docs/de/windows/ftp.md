---
layout: page
title: windows/ftp (Deutsch)
description: "Interaktiver Dateitransfer zwischen einem lokalen und einem entfernten FTP-Server."
content_hash: b117ea8068d2ce0ec1da4e78afa77d9a7ea34fd3
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/ftp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/ftp.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/ftp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ftp

Interaktiver Dateitransfer zwischen einem lokalen und einem entfernten FTP-Server.
Weitere Informationen: <https://learn.microsoft.com/windows-server/administration/windows-commands/ftp>.

- Verbinden mit einem entfernten FTP-Server:

`ftp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Anmelden als anonymer Benutzer:

`ftp -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Deaktivieren der automatische Anmeldung bei der ersten Verbindung:

`ftp -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Ausführen einer Datei, die eine Liste von FTP-Befehlen enthält:

`ftp -s:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Pfad/zur/Datei</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Herunterladen von mehrerern Dateien (globaler Ausdruck):

`mget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.png</span>

- Hochladen von mehrerern Dateien (globaler Ausdruck):

`mput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.zip</span>

- Löschen mehrerer Dateien auf dem entfernten Server:

`mdelete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>

- Ausführliche Hilfe anzeigen:

`ftp --help`
