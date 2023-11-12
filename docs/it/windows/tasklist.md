---
layout: page
title: windows/tasklist (italiano)
description: "Mostra una lista dei processi in esecuzione su una macchina locale o remota."
content_hash: 623fe87b641adf50e5b5315d3cfd72326c423fe3
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/tasklist.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/tasklist.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tasklist

Mostra una lista dei processi in esecuzione su una macchina locale o remota.
Maggiori informazioni: <https://learn.microsoft.com/windows-server/administration/windows-commands/tasklist>.

- Mostra i processi in esecuzione:

`tasklist`

- Mostra i processi in esecuzione in un formato specifico:

`tasklist /fo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table|list|csv</span>

- Mostra i processi in esecuzione utilizzando il nome del file `.exe` o `.dll` specificato:

`tasklist /m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern_di_moduli</span>

- Mostra i processi in esecuzione su una macchina remota:

`tasklist /s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_macchina_remota</span>` /u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_utente</span>` /p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- Visualizzare i servizi utilizzando ogni processo:

`tasklist /svc`
