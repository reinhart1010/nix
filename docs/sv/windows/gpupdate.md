---
layout: page
title: windows/gpupdate (svenska)
description: "Ett verktyg för att kontrollera och uppdatera Windows Group Policy settings."
content_hash: a8fca28047669800287ad8fc345e0f686840ce54
related_topics:
  - title: English version
    url: /en/windows/gpupdate.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># gpupdate

Ett verktyg för att kontrollera och uppdatera Windows Group Policy settings.
Mer information: <https://learn.microsoft.com/windows-server/administration/windows-commands/gpupdate>.

- Kontrollera och tillämpa uppdaterade Group Policy settings:

`gpupdate`

- Ange för vilka Group Policy inställningar du vill kontrollera för uppdateringar:

`gpupdate /target:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datornamn|användare</span>

- Tvinga alla Group Policy inställningar att tillämpas igen:

`gpupdate /force`

- Visa detaljerad användningsinformation:

`gpupdate /?`
