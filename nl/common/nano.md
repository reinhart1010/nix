---
layout: page
title: common/nano (Nederlands)
description: "Simpele, makkelijk te gebruiken command-line tekst bewerker. Een verbeterde, gratis Pico kloon."
content_hash: 384c5029a903075e6fa811e60895d21d0ed1a3cd
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

Simpele, makkelijk te gebruiken command-line tekst bewerker. Een verbeterde, gratis Pico kloon.
Meer informatie: <https://nano-editor.org>.

- Open een nieuw bestand in nano:

`nano`

- Open een specifiek bestand:

`nano `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Open een bepaald bestand, met de cursor gezet in een gegeven regel en kolom:

`nano +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regel</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kolom</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Open een bepaald bestand en zet 'soft wrapping' aan:

`nano --softwrap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Open een bepaald bestand en spring nieuwe regels in volgens de inspringing van de vorige regel:

`nano --autoindent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Open nano en maak een reservekopie (`bestand~`) bij het opslaan van veranderingen:

`nano --backup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
