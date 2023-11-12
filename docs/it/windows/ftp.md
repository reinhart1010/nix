---
layout: page
title: windows/ftp (italiano)
description: "Trasferisci file in modo interattivo tra un server FTP locale e remoto."
content_hash: f84b8a1703faf7f3c1bf860c139df0eb9bd0e2b2
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/ftp.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/ftp.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/ftp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ftp

Trasferisci file in modo interattivo tra un server FTP locale e remoto.
Maggiori informazioni: <https://learn.microsoft.com/windows-server/administration/windows-commands/ftp>.

- Connettiti a un server FTP remoto:

`ftp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Accedi come utente anonimo:

`ftp -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Disabilita l'accesso automatico alla connessione iniziale:

`ftp -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Esegui un file contenente una lista di comandi FTP:

`ftp -s:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso\to\file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Carica file (espressione glob):

`mget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.png</span>

- Carica file (espressione glob):

`mput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.zip</span>

- Cancella file sul server remoto:

`mdelete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>

- Mostra la pagina di aiuto dettagliato:

`ftp --help`
