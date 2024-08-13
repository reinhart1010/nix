---
layout: page
title: windows/for (Nederlands)
description: "Voer conditioneel een commando meerdere keren uit."
content_hash: 90e3183ef271ea80d9bde553716ac32ffba8bb41
last_modified_at: 2024-08-13
related_topics:
  - title: English version
    url: /en/windows/for.html
    icon: bi bi-globe
tldri18n_status: 2
---
# for

Voer conditioneel een commando meerdere keren uit.
Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/for>.

- Voer de gegeven commando's uit voor de opgegeven set:

`for %`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabele</span>` in (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">item_a item_b item_c</span>`) do (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Loop wordt uitgevoerd</span>`)`

- Itereer over een gegeven reeks nummers:

`for /l %`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabele</span>` in (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">van</span>`, `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stap</span>`, `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tot</span>`) do (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Loop wordt uitgevoerd</span>`)`

- Itereer over een gegeven lijst van bestanden:

`for %`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabele</span>` in (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand1.ext pad\naar\bestand2.ext ...</span>`) do (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Loop wordt uitgevoerd</span>`)`

- Itereer over een gegeven lijst van directories:

`for /d %`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabele</span>` in (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\directory1.ext pad\naar\directory2.ext ...</span>`) do (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Loop wordt uitgevoerd</span>`)`

- Voer een gegeven commando uit in elke directory:

`for /d %`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabele</span>` in (*) do (if exist %`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabele</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Loop wordt uitgevoerd</span>`)`
