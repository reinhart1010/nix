---
layout: page
title: windows/wsl (Deutsch)
description: "Verwalte das Windows Subsystem für Linux von der Kommandozeile."
content_hash: faa557f2af9173442e10a5fd8c0e380f869e360a
related_topics:
  - title: English version
    url: /en/windows/wsl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/wsl.html
    icon: bi bi-globe
---
# wsl

Verwalte das Windows Subsystem für Linux von der Kommandozeile.
Weitere Informationen: <https://learn.microsoft.com/windows/wsl/reference>.

- Starte eine Linux-Shell (in der Standard-Distribution):

`wsl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell_befehl</span>

- Führe einen Linux-Befehl aus, ohne eine Shell zu benutzen:

`wsl --exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl_argumente</span>

- Gib eine bestimmte Distribution an:

`wsl --distribution `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">distribution</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell_befehl</span>

- Liste verfügbare Distributionen auf:

`wsl --list`

- Exportiere eine Distribution in eine `.tar` Datei:

`wsl --export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">distribution</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.tar</span>

- Importiere eine Distribution von einer `.tar` Datei:

`wsl --import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">distribution</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/installations_verzeichnis</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.tar</span>

- Ändere die WSL-Version einer bestimmten Distribution:

`wsl --set-version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">distribution</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Fahre das Windows Subsystem für Linux herunter:

`wsl --shutdown`
