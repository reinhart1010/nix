---
layout: page
title: common/asciinema (Nederlands)
description: "Neemt op en speelt terminal sessies af en deelt hem optioneel op asciinema.org."
content_hash: 3b39365c81fc5fdee9ba7b4aa9d7c857c20f5ef3
last_modified_at: 2024-09-25
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
  - title: Indonesia version
    url: /id/common/asciinema.html
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

Neemt op en speelt terminal sessies af en deelt hem optioneel op asciinema.org.
Bekijk ook: `terminalizer`.
Meer informatie: <https://docs.asciinema.org/manual/cli/usage>.

- Associeer de lokale installatie van `asciinema` met het asciinema.org account:

`asciinema auth`

- Maak een nieuwe opname (gebruiker krijgt een vraag om het lokaal op te slaan of te uploaden als de opname klaar is):

`asciinema rec`

- Maak een nieuwe opname en sla het op in een lokaal bestand:

`asciinema rec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/opname.cast</span>

- Speel een terminal opname af vanaf een lokaal bestand:

`asciinema play `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/opname.cast</span>

- Speel een terminal opname af vanaf asciinema.org:

`asciinema play https://asciinema.org/a/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cast_id</span>

- Maak een nieuwe opname met een [i]nactieve tijd van maximaal 2,5 seconden:

`asciinema rec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--idle-time-limit</span>` 2.5`

- Laat de volledige inhoud zien van een lokaal opgeslagen opname:

`asciinema cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/opname.cast</span>

- Sla een lokaal opgeslagen terminal sessie op bij asciinema.org:

`asciinema upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/opname.cast</span>
