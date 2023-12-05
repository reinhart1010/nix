---
layout: page
title: windows/move (Nederlands)
description: "Verplaats of hernoem bestanden en mappen."
content_hash: 9b6341e0cfcea03251df620bc242a2763c4e1559
last_modified_at: 2023-12-05
related_topics:
  - title: English version
    url: /en/windows/move.html
    icon: bi bi-globe
tldri18n_status: 2
---
# move

Verplaats of hernoem bestanden en mappen.
In PowerShell is dit commando een alias van `Move-Item`. Deze documentatie is gebaserd op de  Command Prompt (`cmd`) versie van `move`.
Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/move>.

- Bekijk de documentatie van het PowerShell equivalente commando:

`tldr move-item`

- Hernoem een bestand of map als het doel een niet-bestaande map is:

`move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bron</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\doel</span>

- Verplaats een bestand of map naar een bestaande map:

`move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bron</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestaande_map</span>

- Verplaats een map of bestand naar een andere schijf:

`move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:\pad\naar\bron</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">D:\pad\naar\doel</span>

- Vraag niet voor bevestiging voordat bestaande bestanden worden overschreven:

`move /Y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bron</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestaande_map</span>

- Vraag voor bevestiging voordat bestaande bestanden worden overschreven, ongeacht de bestandspermissies:

`move /-Y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bron</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestaande_map</span>
