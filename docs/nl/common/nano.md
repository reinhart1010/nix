---
layout: page
title: common/nano (Nederlands)
description: "Command-line tekst bewerker. Een verbeterde `Pico` kloon."
content_hash: 7dfedda5909997f3a7653060e4408de135219ec5
last_modified_at: 2023-11-02
related_topics:
  - title: English version
    url: /en/common/nano.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/nano.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/nano.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/nano.html
    icon: bi bi-globe
---
# nano

Command-line tekst bewerker. Een verbeterde `Pico` kloon.
Meer informatie: <https://nano-editor.org>.

- Start de tekst bewerker:

`nano`

- Start de tekst bewerker zonder gebruik te maken van configuratiebestanden:

`nano --ignorercfiles`

- Open specifieke bestanden, ga naar het volgende bestand bij het sluiten van de vorige:

`nano `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>

- Open een bestand en positioneer de cursor op een specifieke regel en kolom:

`nano +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regel</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kolom</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Open een bestand en zet 'soft wrapping' aan:

`nano --softwrap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Open een bestand en spring nieuwe regels in volgens de inspringing van de vorige regel:

`nano --autoindent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Open een bestand en maak een reservekopie (`pad/naar/bestand~`) bij het opslaan:

`nano --backup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
