---
layout: page
title: windows/chkdsk (italiano)
description: "Controlla il file system e i metadata dei dischi per cercare errori."
content_hash: 1317c5cea6ecdbed3c04b907c3688cfef23f8d0d
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/chkdsk.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/chkdsk.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/chkdsk.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/windows/chkdsk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chkdsk

Controlla il file system e i metadata dei dischi per cercare errori.
Maggiori informazioni: <https://learn.microsoft.com/windows-server/administration/windows-commands/chkdsk>.

- Specifica la lettera del disco (seguita da due punti ':'), monta una partizione o un disco da controllare:

`chkdsk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">disco</span>

- Ripara gli errori di un disco specifico:

`chkdsk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">disco</span>` /f`

- Smonta un disco specifico prima di eseguire il controllo:

`chkdsk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume</span>` /x`

- Cambia la dimensione dei file di log in una dimensione specifica (solo per NTFS):

`chkdsk /l`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dimensione</span>
