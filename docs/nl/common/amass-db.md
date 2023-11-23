---
layout: page
title: common/amass-db (Nederlands)
description: "Interactie met een Amass database."
content_hash: aad661085d04a2e7187564a7bd3ee73a5e780ade
last_modified_at: 2023-11-23
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
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/amass-db.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

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
