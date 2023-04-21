---
layout: page
title: common/powershell (italiano)
description: "Shell della riga di comando e linguaggio di scripting progettato appositamente per l'amministrazione dei sistemi."
content_hash: 74335404d1340756bd11152a9e596272f1db5a3b
last_modified_at: 2023-04-21
related_topics:
  - title: English version
    url: /en/common/powershell.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/powershell.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># powershell

Shell della riga di comando e linguaggio di scripting progettato appositamente per l'amministrazione dei sistemi.
Guarda anche: `pwsh`.
Maggiori informazioni: <https://learn.microsoft.com/windows-server/administration/windows-commands/powershell>.

- Avvia una sessione di shell interattiva:

`powershell`

- Avvia una sessione shell interattiva senza caricare le configurazioni di avvio:

`powershell -NoProfile`

- Esegui specifici comandi:

`powershell -Command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'powershell è eseguito'</span>`"`

- Esegui uno specifico script:

`powershell -File `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/dello/script.ps1</span>

- Avvia una sessione con una versione specifica di PowerShell:

`powershell -Version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versione</span>

- Impedisci l'uscita dalla shell dopo aver eseguito i comandi di avvio:

`powershell -NoExit`

- Specifica il formato dei dati inviati a PowerShell:

`powershell -InputFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Text|XML</span>

- Specifica come formattatare l'output da PowerShell:

`powershell -OutputFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Text|XML</span>
