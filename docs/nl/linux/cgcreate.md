---
layout: page
title: linux/cgcreate (Nederlands)
description: "Maak cgroups, gebruikt om bronnen te beperken, te meten en te regelen die door processen worden gebruikt."
content_hash: 75a48effd7e8bd432f60f843671b3176a86204c1
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/linux/cgcreate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cgcreate

Maak cgroups, gebruikt om bronnen te beperken, te meten en te regelen die door processen worden gebruikt.
`cgroups` types kunnen een van `memory`, `cpu`, `net_cls`, etc. zijn.
Meer informatie: <https://manned.org/cgcreate>.

- Maak een nieuwe groep:

`cgcreate -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groep_type</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groepsnaam</span>

- Maak een nieuwe groep met meerdere cgroep typen:

`cgcreate -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groep_type1</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groep_type2</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groepsnaam</span>

- Maak een subgroep:

`mkdir /sys/fs/cgroup/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groep_type</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groepsnaam</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subgroep_naam</span>
