---
layout: page
title: linux/updatedb (Nederlands)
description: "Maak of werk de database bij die gebruikt wordt door `locate`."
content_hash: f8e228ce9f14457131e10ce01ad3396424f57024
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/linux/updatedb.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/updatedb.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># updatedb

Maak of werk de database bij die gebruikt wordt door `locate`.
Dit wordt meestal dagelijks uitgevoerd door cron.
Meer informatie: <https://manned.org/updatedb>.

- Ververs de inhoud van de database:

`sudo updatedb`

- Toon bestandsnamen zodra ze gevonden zijn:

`sudo updatedb --verbose`
