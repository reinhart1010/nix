---
layout: page
title: linux/cgcreate (Nederlands)
description: "Maak cgroups, gebruikt om bronnen te beperken, te meten en te regelen die door processen worden gebruikt."
content_hash: 36865f3d6783913a7397281890c368bfb3f51552
last_modified_at: 2023-11-26
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

`cgcreate -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_type</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>

- Maak een nieuwe groep met meerdere cgroep typen:

`cgcreate -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_type1</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_type2</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>

- Maak een subgroep:

`mkdir /sys/fs/cgroup/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_type</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subgroup_name</span>
