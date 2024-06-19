---
layout: page
title: linux/groupadd (Nederlands)
description: "Voeg gebruikersgroepen toe aan het systeem."
content_hash: 2ed027030a47e1ff64a878d3c3a9c735418c209c
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/linux/groupadd.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/groupadd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# groupadd

Voeg gebruikersgroepen toe aan het systeem.
Bekijk ook: `groups`, `groupdel`, `groupmod`.
Meer informatie: <https://manned.org/groupadd>.

- Maak een nieuwe groep aan:

`sudo groupadd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groepsnaam</span>

- Maak een nieuwe systeemgroep aan:

`sudo groupadd --system `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groepsnaam</span>

- Maak een nieuwe groep aan met een specifieke groeps-ID:

`sudo groupadd --gid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groepsnaam</span>
