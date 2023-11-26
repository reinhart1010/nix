---
layout: page
title: common/pwsh (Nederlands)
description: "Command-line shell en scripting taal specifiek ontworpen voor systeemadministratie."
content_hash: 0635706eeaa9d2f823d8f918a0120a9571ed4bbd
last_modified_at: 2023-11-26
related_topics:
  - title: English version
    url: /en/common/pwsh.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/pwsh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pwsh

Command-line shell en scripting taal specifiek ontworpen voor systeemadministratie.
Dit commando refereert naar PowerShell versie 6 en hoger (ook wel bekend als  PowerShell Core en cross-platform PowerShell).
Om de originele Windows versie (5.1 en lager, ook wel bekend als de legacy Windows PowerShell) te gebruiken, gebruik `powershell` in plaats van `pwsh`.
Meer informatie: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_pwsh>.

- Start een interactieve shell sessie:

`pwsh`

- Start een interactieve shell sessie zonder het laden van startup configuraties:

`pwsh -NoProfile`

- Voer specifieke commando's uit:

`pwsh -Command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'powershell is uitgevoerd'</span>`"`

- Voer een specifiek script uit:

`pwsh -File `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/script.ps1</span>

- Start een sessie met een specifieke versie van PowerShell:

`pwsh -Version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versie</span>

- Voorkom dat een shell afsluit na het uitvoeren van de opstart-commando's:

`pwsh -NoExit`

- Beschrijf het formaat van de data die gestuurd word naar to PowerShell:

`pwsh -InputFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Text|XML</span>

- Bepaal hoe een uitvoer van Powershell word geformateerd:

`pwsh -OutputFormat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Text|XML</span>
