---
layout: page
title: common/knotc (español)
description: "Controla el servidor DNS knot."
content_hash: 8d9290bf9dbde0a820f29b427cd567dbc5c38152
last_modified_at: 2024-07-02
related_topics:
  - title: English version
    url: /en/common/knotc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# knotc

Controla el servidor DNS knot.
Más información: <https://www.knot-dns.cz/docs/latest/html/man_knotc.html>.

- Comienza a editar una zona:

`knotc zone-begin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zona</span>

- Establece un registro A con TTL de 3600:

`knotc zone-set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zona</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subdominio</span>` 3600 A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_ip</span>

- Finaliza la edición de la zona:

`knotc zone-commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zona</span>

- Obtén los datos de la zona actual:

`knotc zone-read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zona</span>

- Obtén la configuración actual del servidor:

`knotc conf-read server`
