---
layout: page
title: linux/trash (Nederlands)
description: "Beheer de prullenbak."
content_hash: 3cd42c973563b1f0ef692dd5a670be9233bc5ff0
last_modified_at: 2024-09-13
related_topics:
  - title: English version
    url: /en/linux/trash.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/trash.html
    icon: bi bi-globe
tldri18n_status: 2
---
# trash

Beheer de prullenbak.
Meer informatie: <https://github.com/andreafrancia/trash-cli>.

- Verplaats een bestand naar de prullenbak:

`trash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon alle bestanden in de prullenbak:

`trash-list`

- Herstel een bestand uit de prullenbak (interactief):

`trash-restore`

- Leeg de prullenbak:

`trash-empty`

- Verwijder permanent alle bestanden in de prullenbak die ouder zijn dan 10 dagen:

`trash-empty 10`

- Verwijder alle bestanden in de prullenbak die overeenkomen met een specifiek blob-patroon:

`trash-rm "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.o</span>`"`

- Verwijder alle bestanden met een specifieke oorspronkelijke locatie:

`trash-rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/pad/naar/bestand_of_map</span>
