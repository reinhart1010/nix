---
layout: page
title: common/expand (italiano)
description: "Converti caratteri tab in spazi."
content_hash: d5df26f2e4eb30a879dff29e7b68b7065af5f0a6
related_topics:
  - title: English version
    url: /en/common/expand.html
    icon: bi bi-globe
---
# expand

Converti caratteri tab in spazi.
Maggiori informazioni: <https://www.gnu.org/software/coreutils/expand>.

- Converti tab in un file in spazi, scrivendo su standard output:

`expand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Converti i tab in spazi, leggendo da standard input:

`expand`

- Non convertire i tab dopo caratteri di spaziatura:

`expand -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Sostituisci i tab con un determinato numeroo di spazi, non 8 (default):

`expand -t=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_spazi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Utilizza una lista separata da virgole di posizioni esplicite di tab:

`expand -t=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1,4,6</span>
