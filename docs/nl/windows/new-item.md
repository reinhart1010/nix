---
layout: page
title: windows/new-item (Nederlands)
description: "Maak een nieuw bestand, directory, symbolische link of een registerinvoer."
content_hash: 78eac4d6df9d654c96f327a97f99705d1633fa9f
last_modified_at: 2023-11-26
related_topics:
  - title: English version
    url: /en/windows/new-item.html
    icon: bi bi-globe
tldri18n_status: 2
---
# New-Item

Maak een nieuw bestand, directory, symbolische link of een registerinvoer.
Dit commando kan alleen worden uitgevoerd onder PowerShell.
Meer informatie: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/new-item>.

- Maak een nieuw leeg bestand (gelijk aan `touch`):

`New-Item `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand</span>

- Maak een nieuwe map:

`New-Item -ItemType Directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\map</span>

- Schrijf een nieuw tekstbestand met opgegeven inhoud:

`New-Item `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand</span>` -Value `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">content</span>

- Schrijf hetzelfde tekstbestand op meerdere locaties:

`New-Item `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand1 , pad\naar\bestand2 , ...</span>` -Value `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">content</span>

- Maak een symbolische link\harde link\junction naar een bestand of map:

`New-Item -ItemType `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SymbolicLink|HardLink|Junction</span>` -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\link_file</span>` -Target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bronbestand_of_map</span>

- Maak een nieuw lege registerinvoer (in REG_SZ, gebruik `New-ItemProperty` of `Set-ItemProperty` om het waardetype te verfijnen):

`New-Item `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\registersleutel</span>

- Maak een nieuw lege registerinvoer met gespecificeerde waarde:

`New-Item `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\registersleutel</span>` -Value `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>
