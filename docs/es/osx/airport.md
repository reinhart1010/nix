---
layout: page
title: osx/airport (español)
description: "Utilidad de configuración de red inalámbrica."
content_hash: 8f2e075bd9eb2f9a90abf358790de6cb720fe1f4
last_modified_at: 2023-11-12
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

`airport -I`

- Detecta tráfico inalámbrico en el canal 1:

`airport sniff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Busca redes inalámbricas disponibles:

`airport -s`

- Desasociarse de la red actual:

`sudo airport -z`
