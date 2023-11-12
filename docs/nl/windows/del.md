---
layout: page
title: windows/del (Nederlands)
description: "Verwijder een of meer bestanden."
content_hash: 7284309269bcf23e33e067b90ff298485249ecb9
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/del.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/del.html
    icon: bi bi-globe
  - title: español version
    url: /es/windows/del.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/del.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/del.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/del.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/del.html
    icon: bi bi-globe
tldri18n_status: 2
---
# del

Verwijder een of meer bestanden.
In PowerShell is dit commando een alias van `Remove-Item`. Deze documentatie is gebaseerd op de Command Prompt (`cmd`) versie van `del`.
Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/del>.

- Bekijk de documentatie van het equivalente PowerShell commando:

`tldr remove-item`

- Verwijder een of meer, door spatie gescheiden, bestanden of patronen:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_pattern</span>

- Vraag om bevestiging voordat u elk bestand verwijdert:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_pattern</span>` /p`

- Forceer de verwijdering van alleen-lezen bestanden:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_pattern</span>` /f`

- Verwijder de bestand(en) recursief uit alle submappen:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_pattern</span>` /s`

- Vraag niet om bevestiging voor het verwijderen van bestanden gebaseerd op een globale wildcard:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_pattern</span>` /q`

- Geef de beschikbare hulp en lijst met attributen weer:

`del /?`

- Verwijder bestanden op basis van opgegeven kenmerken:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_pattern</span>` /a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">attribute</span>
