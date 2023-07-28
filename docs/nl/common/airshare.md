---
layout: page
title: common/airshare (Nederlands)
description: "Gegevens overdragen tussen twee machines in een lokaal netwerk."
content_hash: adff579d262408a726757ecf2a165527728fdd45
last_modified_at: 2023-07-28
related_topics:
  - title: English version
    url: /en/common/airshare.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># airshare

Gegevens overdragen tussen twee machines in een lokaal netwerk.
Meer informatie: <https://airshare.rtfd.io/en/latest/cli.html>.

- Bestanden of mappen delen:

`airshare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_directory1 pad/naar/bestand_of_directory2 ...</span>

- Ontvang een bestand:

`airshare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>

- Host een ontvangende server (gebruik deze om bestanden te kunnen uploaden via de webinterface):

`airshare --upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>

- Stuur bestanden of mappen naar een ontvangende server:

`airshare --upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_directory1 pad/naar/bestand_of_directory2 ...</span>

- Bestanden verzenden waarvan de paden naar het klembord zijn gekopieerd:

`airshare --file-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>

- Ontvang een bestand en kopieer het naar het klembord:

`airshare --clip-receive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>
