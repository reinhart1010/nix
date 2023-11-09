---
layout: page
title: common/amass-db (Nederlands)
description: "Interactie met een Amass database."
content_hash: aad661085d04a2e7187564a7bd3ee73a5e780ade
last_modified_at: 2023-11-09
related_topics:
  - title: English version
    url: /en/common/amass-db.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/amass-db.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/amass-db.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># amass db

Interactie met een Amass database.
Meer informatie: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-db-subcommand>.

- Toon alle uitgevoerde opsommingen in de database:

`amass db -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/database_map</span>` -list`

- Toon de resultaten van een specifieke opsommingsindex en domeinnaam:

`amass db -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/database_map</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domeinnaam</span>` -enum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indexlijst</span>` -show`

- Toon alle gevonden subdomeinen van een domeinnaam binnen de opsomming:

`amass db -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/database_map</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domeinnaam</span>` -enum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indexlijst</span>` -names`

- Toon een samenvatting van de gevonden subdomeinen binnen de opsomming:

`amass db -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/database_map</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domeinnaam</span>` -enum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indexlijst</span>` -summary`
