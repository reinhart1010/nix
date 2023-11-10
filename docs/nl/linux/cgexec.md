---
layout: page
title: linux/cgexec (Nederlands)
description: "Beperk, meet en beheers bronnen die door processen worden gebruikt."
content_hash: b6a9331ab44a268e768dd21cfdd668c5d5b387ff
last_modified_at: 2023-11-10
related_topics:
  - title: English version
    url: /en/linux/cgexec.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cgexec

Beperk, meet en beheers bronnen die door processen worden gebruikt.
Er bestaan meerdere cgroup types (oftwel controllers), zoals `cpu`, `memory`, etc.
Meer informatie: <https://manned.org/cgexec>.

- Voer een proces uit in een bepaalde cgroup met een bepaalde controller:

`cgexec -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">controller</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cgroup_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>
