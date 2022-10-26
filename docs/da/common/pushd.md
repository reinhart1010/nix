---
layout: page
title: common/pushd (dansk)
description: "Tilføj en mappe til mappe-stakken, så den kan tilgås på et senere tidspunkt."
content_hash: 505775560a08fba879dbdf3bec9580e9a35d7cfd
related_topics:
  - title: English version
    url: /en/common/pushd.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pushd

Tilføj en mappe til mappe-stakken, så den kan tilgås på et senere tidspunkt.
Se `popd` for at skifte tilbage til den oprindelige mappe og `dirs` for at vise indholdet af mappe-stakken.
Mere information: <https://www.gnu.org/software/bash/manual/html_node/Directory-Stack-Builtins.html>.

- Skift til mappe og tilføj den til mappe-stakken:

`pushd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mappe</span>

- Byt om på første og anden mappe i mappe-stakken:

`pushd`

- Rotér mappe-stakken ved at gøre det femte element til det første i mappe-stakken.

`pushd +4`
