---
layout: page
title: windows/remove-item (Nederlands)
description: "Verwijder bestanden, mappen, evenals registersleutels en subkeys."
content_hash: 40c356840268d97671a76f8012aa9e336266ef7f
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/remove-item.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Remove-Item

Verwijder bestanden, mappen, evenals registersleutels en subkeys.
Deze opdracht kan alleen door PowerShell worden uitgevoerd.
Meer informatie: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/remove-item>.

- Verwijder specifieke bestanden of registersleutels (zonder subkeys):

`Remove-Item `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand_of_key1 pad\naar\bestand_of_key2 ...</span>

- Verwijder verborgen of alleen-lezen bestanden:

`Remove-Item -Force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand1 pad\naar\bestand2 ...</span>

- Verwijder specifieke bestanden of registersleutels interactief gevraagd vóór elke verwijdering:

`Remove-Item -Confirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand_of_key1 pad\naar\bestand_of_key2 ...</span>

- Verwijder specifieke bestanden en mappen recursief (Windows 10 versie 1909 of hoger):

`Remove-Item -Recurse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand_of_map1 pad\naar\bestand_of_map2 ...</span>

- Verwijder specifieke Windows-registersleutels en al zijn subkeys:

`Remove-Item -Recurse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\key1 pad\naar\key2 ...</span>

- Voer een dry-run van het verwijderproces uit:

`Remove-Item -WhatIf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand1 pad\naar\bestand2 ...</span>
