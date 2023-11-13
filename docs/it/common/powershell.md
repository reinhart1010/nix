---
layout: page
title: common/powershell (italiano)
description: "Shell della riga di comando e linguaggio di scripting progettato appositamente per l'amministrazione dei sistemi."
content_hash: fb8835fd139dcc9357a4128b37b6e24b4b3bfa1d
last_modified_at: 2023-11-13
related_topics:
  - title: English version
    url: /en/common/powershell.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/powershell.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/powershell.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/powershell.html
    icon: bi bi-globe
tldri18n_status: 2
---
# powershell

Shell della riga di comando e linguaggio di scripting progettato appositamente per l'amministrazione dei sistemi.
Guarda anche: `pwsh`.
Maggiori informazioni: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_pwsh>.

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
