---
layout: page
title: linux/locate (Nederlands)
description: "Vind snel bestandsnamen."
content_hash: 5d713fcea3aba59c9149be6991dd7fbb6c4a2ce5
last_modified_at: 2024-06-19
related_topics:
  - title: Deutsch version
    url: /de/linux/locate.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/locate.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/locate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# locate

Vind snel bestandsnamen.
Meer informatie: <https://manned.org/locate>.

- Zoek naar een patroon in de database. Opmerking: de database wordt periodiek herberekend (meestal wekelijks of dagelijks):

`locate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patroon</span>

- Zoek naar een bestand op basis van de exacte bestandsnaam (een patroon zonder glob-tekens wordt geïnterpreteerd als `*patroon*`):

`locate '*/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestandsnaam</span>`'`

- Herbereken de database. Dit moet je doen als je recent toegevoegde bestanden wilt vinden:

`sudo updatedb`
