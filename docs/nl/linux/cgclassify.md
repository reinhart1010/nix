---
layout: page
title: linux/cgclassify (Nederlands)
description: "Verplaats lopende taken naar opgegeven `cgroups`."
content_hash: 9d6c36436613d0645d3216bf57e030f82650253e
last_modified_at: 2023-11-26
related_topics:
  - title: English version
    url: /en/linux/cgclassify.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cgclassify

Verplaats lopende taken naar opgegeven `cgroups`.
Meer informatie: <https://manned.org/cgclassify>.

- Verplaats het proces met een specifiek PID naar de controle groep student in de CPU hierarchie:

`cgclassify -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cpu:student</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>

- Verplaats het proces met een specifiek PID naar de controle groepen gebaseerd op het `/etc/cgrules.conf` configuratie bestand:

`cgclassify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>

- Verplaats het proces met een specifiek PID naar de controle groep student in de CPU hierarchy. Let op: de daemon van de service `cgred` veranderd `cgroups` van de specifieke PID en zijn onderliggende processen niet (gebaseerd op `/etc/cgrules.conf`):

`cgclassify --sticky -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cpu:/student</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>
