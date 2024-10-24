---
layout: page
title: linux/pihole (español)
description: "Interfaz de terminal para el servidor DNS de bloqueo de anuncios Pi-hole."
content_hash: 23997b502e5e0157ff6fde9f080bf7ce2745a72d
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/linux/pihole.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pihole

Interfaz de terminal para el servidor DNS de bloqueo de anuncios Pi-hole.
Más información: <https://docs.pi-hole.net/core/pihole-command/>.

- Verifica el estado del daemon de Pi-hole:

`pihole status`

- Actualiza Pi-hole y Gravity:

`pihole -up`

- Monitorea el estado detallado del sistema:

`pihole chronometer`

- Inicia o detiene el daemon:

`pihole `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enable|disable</span>

- Reinicia el daemon (no el servidor en sí):

`pihole restartdns`

- Incluye en lista blanca o negra un dominio:

`pihole `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">whitelist|blacklist</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ejemplo.com</span>

- Busca en las listas un dominio:

`pihole query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ejemplo.com</span>

- Abre un registro de conexiones en tiempo real:

`pihole tail`
