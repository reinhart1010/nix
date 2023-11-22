---
layout: page
title: linux/cgclassify (Nederlands)
description: "Verplaats lopende taken naar opgegeven `cgroups`."
content_hash: 9d6c36436613d0645d3216bf57e030f82650253e
last_modified_at: 2023-11-22
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/cgclassify.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cgclassify

Verplaats lopende taken naar opgegeven `cgroups`.
Meer informatie: <https://manned.org/cgclassify>.

- Verplaats het proces met een specifiek PID naar de controle groep student in de CPU hierarchie:

`cgclassify -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cpu:student</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>

- Verplaats het proces met een specifiek PID naar de controle groepen gebaseerd op het `/etc/cgrules.conf` configuratie bestand:

`cgclassify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>

- Verplaats het proces met een specifiek PID naar de controle groep student in de CPU hierarchy. Let op: de daemon van de service `cgred` veranderd `cgroups` van de specifieke PID en zijn onderliggende processen niet (gebaseerd op `/etc/cgrules.conf`):

`cgclassify --sticky -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cpu:/student</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>
