---
layout: page
title: common/expand (italiano)
description: "Converti caratteri tab in spazi."
content_hash: e83e0b2f4097a652cad6b76723eb6562692ec548
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/expand.html
    icon: bi bi-globe
tldri18n_status: 2
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

- Sostituisci i tab con un determinato numero di spazi, non 8 (default):

`expand -t=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_spazi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Utilizza una lista separata da virgole di posizioni esplicite di tab:

`expand -t=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1,4,6</span>
