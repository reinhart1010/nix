---
layout: page
title: linux/updatedb (Nederlands)
description: "Maak of werk de database bij die gebruikt wordt door `locate`."
content_hash: f8e228ce9f14457131e10ce01ad3396424f57024
last_modified_at: 2024-06-20
related_topics:
  - title: English version
    url: /en/linux/updatedb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# updatedb

Maak of werk de database bij die gebruikt wordt door `locate`.
Dit wordt meestal dagelijks uitgevoerd door cron.
Meer informatie: <https://manned.org/updatedb>.

- Ververs de inhoud van de database:

`sudo updatedb`

- Toon bestandsnamen zodra ze gevonden zijn:

`sudo updatedb --verbose`
