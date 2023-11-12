---
layout: page
title: common/airshare (Nederlands)
description: "Gegevens overdragen tussen twee machines in een lokaal netwerk."
content_hash: 0ae0960588797e21ec39e528e28ffdf1edcc7d0b
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/airshare.html
    icon: bi bi-globe
tldri18n_status: 2
---
# airshare

Gegevens overdragen tussen twee machines in een lokaal netwerk.
Meer informatie: <https://airshare.rtfd.io/en/latest/cli.html>.

- Bestanden of mappen delen:

`airshare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map1 pad/naar/bestand_of_map2 ...</span>

- Ontvang een bestand:

`airshare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>

- Host een ontvangende server (gebruik deze om bestanden te kunnen uploaden via de webinterface):

`airshare --upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>

- Stuur bestanden of mappen naar een ontvangende server:

`airshare --upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map1 pad/naar/bestand_of_map2 ...</span>

- Bestanden verzenden waarvan de paden naar het klembord zijn gekopieerd:

`airshare --file-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>

- Ontvang een bestand en kopieer het naar het klembord:

`airshare --clip-receive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>
