---
layout: page
title: common/pushd (dansk)
description: "Tilføj en mappe til mappe-stakken, så den kan tilgås på et senere tidspunkt."
content_hash: 5046d0177ebd648928dce285848af946be10d0e3
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/pushd.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/pushd.html
    icon: bi bi-globe
tldri18n_status: 1
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

- Rotér mappe-stakken ved at gøre det femte element til det første i mappe-stakken:

`pushd +4`
