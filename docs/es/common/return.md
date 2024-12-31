---
layout: page
title: common/return (español)
description: "Sale de una función o un script si se ejecuta con `source`."
content_hash: b6513164f1f8b360152b0c8dae4ab426121d0f9d
last_modified_at: 2024-12-31
related_topics:
  - title: English version
    url: /en/common/return.html
    icon: bi bi-globe
tldri18n_status: 2
---
# return

Sale de una función o un script si se ejecuta con `source`.
Más información: <https://www.gnu.org/software/bash/manual/bash.html#index-return>.

- Sale prematuramente de una función:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_función</span>`() { `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "Se ha alcanzado"</span>`; return; `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "No se ha alcanzado"</span>`; }`

- Especifica el valor de retorno de la función:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_función</span>`() { return `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>`; }`
