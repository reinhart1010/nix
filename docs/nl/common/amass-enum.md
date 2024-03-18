---
layout: page
title: common/amass-enum (Nederlands)
description: "Vind subdomeinen van een domein."
content_hash: eec7f44e4256f80fe6438b87400290a933f9f4ad
last_modified_at: 2024-03-18
related_topics:
  - title: English version
    url: /en/common/amass-enum.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/amass-enum.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/amass-enum.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># amass enum

Vind subdomeinen van een domein.
Meer informatie: <https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md#the-enum-subcommand>.

- Vind, passief, subdomeinen van een [d]omein:

`amass enum -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domeinnaam</span>

- Zoek subdomeinen van een [d]omein en verifieer ze actief in een poging de gevonden subdomeinen op te lossen:

`amass enum -active -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domeinnaam</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80,443,8080</span>

- Doe een brute force zoekopdracht op een sub[d]omein:

`amass enum -brute -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domeinnaam</span>

- Sla de resultaten op in een tekstbestand:

`amass enum -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uitvoer_bestand</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domeinnaam</span>

- Sla de resultaten op in een database en andere gedetailleerde output naar een map:

`amass enum -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uitvoer_bestand</span>` -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/database_map</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domeinnaam</span>

- Toon alle beschikbare databronnen:

`amass enum -list`
