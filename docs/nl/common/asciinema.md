---
layout: page
title: common/asciinema (Nederlands)
description: "Neemt en speelt terminal sessies af, en deelt hem optioneel op asciinema.org."
content_hash: 21c7583bde237a70c22470caebe47e7a9b06436b
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/asciinema.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/asciinema.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/asciinema.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/asciinema.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/asciinema.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/asciinema.html
    icon: bi bi-globe
tldri18n_status: 2
---
# asciinema

Neemt en speelt terminal sessies af, en deelt hem optioneel op asciinema.org.
Meer informatie: <https://asciinema.org/docs/usage>.

- Associeer de lokale installatie van `asciinema` met het asciinema.org account:

`asciinema auth`

- Maak een nieuwe opname (gebruiker krijgt een vraag om het lokaal op te slaan of te uploaden als de opname klaar is):

`asciinema rec`

- Maak een nieuwe opname en sla het op in een lokaal bestand:

`asciinema rec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>`.cast`

- Speelt een terminal opname of vanaf een lokaal bestand:

`asciinema play `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>`.cast`

- Speelt een terminal opname of vanaf asciinema.org:

`asciinema play https://asciinema.org/a/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cast_id</span>

- Maakt een nieuwe opname met een inactieve tijd van maximaal 2,5 seconden:

`asciinema rec -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.5</span>

- Laat de volledige inhoud zien van een lokaal opgeslagen opname:

`asciinema cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>`.cast`

- Slaat een lokaal opgeslagen terminal sessie op bij asciinema.org:

`asciinema upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>`.cast`
