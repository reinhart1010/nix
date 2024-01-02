---
layout: page
title: osx/airport (español)
description: "Utilidad de configuración de red inalámbrica."
content_hash: 186e56fd4a00db34bc1fc4ed64ec44915eeb265a
last_modified_at: 2024-01-02
related_topics:
  - title: English version
    url: /en/osx/airport.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/airport.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/airport.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/airport.html
    icon: bi bi-globe
tldri18n_status: 2
---
# airport

Utilidad de configuración de red inalámbrica.
Más información: <https://ss64.com/osx/airport.html>.

- Muestra la información del estado actual de la red inalámbrica:

`airport --getinfo`

- Detecta tráfico inalámbrico en el canal 1:

`airport sniff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Busca redes inalámbricas disponibles:

`airport --scan`

- Desasociarse de la red actual:

`sudo airport --disassociate`
