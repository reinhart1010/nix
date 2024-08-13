---
layout: page
title: windows/if (Nederlands)
description: "Voert voorwaardelijke verwerking uit in batchscripts."
content_hash: 3ef518f2a1dc49b6c4b7a6d3220a3a1dafda4d60
last_modified_at: 2024-08-13
related_topics:
  - title: English version
    url: /en/windows/if.html
    icon: bi bi-globe
tldri18n_status: 2
---
# if

Voert voorwaardelijke verwerking uit in batchscripts.
Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/if>.

- Voer de opgegeven commando's uit als de voorwaarde waar is:

`if `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">voorwaarde</span>` (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Voorwaarde is waar</span>`)`

- Voer de opgegeven commando's uit als de voorwaarde onwaar is:

`if not `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">voorwaarde</span>` (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Voorwaarde is waar</span>`)`

- Voer de eerste opgegeven commando's uit als de voorwaarde waar is, anders voer de tweede opgegeven commando's uit:

`if `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">voorwaarde</span>` (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Voorwaarde is waar</span>`) else (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Voorwaarde is onwaar</span>`)`

- Controleer of `%errorlevel%` groter dan of gelijk is aan de opgegeven exitcode:

`if errorlevel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Voorwaarde is waar</span>`)`

- Controleer of twee strings gelijk zijn:

`if %`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabele</span>`% == `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>` (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Voorwaarde is waar</span>`)`

- Controleer of twee strings gelijk zijn zonder naar hoofdletters te kijken:

`if /i %`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabele</span>`% == `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>` (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Voorwaarde is waar</span>`)`

- Controleer of een bestand bestaat:

`if exist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand</span>` (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Voorwaarde is waar</span>`)`
