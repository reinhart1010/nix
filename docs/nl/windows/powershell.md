---
layout: page
title: windows/powershell (Nederlands)
description: "Command-line shell en scripttaal, ontworpen voor systeembeheer."
content_hash: 0aaa4596647237e7d728f90dfbbcafc84324b7ee
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/windows/powershell.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/powershell.html
    icon: bi bi-globe
tldri18n_status: 2
---
# powershell

Command-line shell en scripttaal, ontworpen voor systeembeheer.
Deze opdracht verwijst naar PowerShell versie 5.1 en lager (ook bekend als legacy Windows PowerShell). Voor de nieuwere, platformonafhankelijke versie van PowerShell (ook bekend als PowerShell Core), gebruik `pwsh` in plaats van `powershell`.
Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/powershell>.

- Start een interactieve shellsessie:

`powershell`

- Start een interactieve shellsessie zonder opstartconfiguraties te laden:

`powershell -NoProfile`

- Voer specifieke commando's uit:

`powershell -Command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'powershell wordt uitgevoerd'</span>`"`

- Voer een specifiek script uit:

`powershell -File `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/script.ps1</span>

- Start een sessie met een specifieke versie van PowerShell:

`powershell -Version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versie</span>

- Voorkom dat een shell afsluit na het uitvoeren van opstartcommando's:

`powershell -NoExit`

- Beschrijf het formaat van gegevens die naar PowerShell worden verzonden:

`powershell -InputFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Text|XML</span>

- Bepaal hoe een output van PowerShell wordt opgemaakt:

`powershell -OutputFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Text|XML</span>
