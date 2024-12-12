---
layout: page
title: linux/ip-rule (español)
description: "Gestión de bases de datos de políticas de enrutamiento IP."
content_hash: 9df3a327789f4412d8d659856077429d9b5a8dd1
last_modified_at: 2024-12-12
related_topics:
  - title: English version
    url: /en/linux/ip-rule.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/ip-rule.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/ip-rule.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ip rule

Gestión de bases de datos de políticas de enrutamiento IP.
Más información: <https://manned.org/ip-rule>.

- Muestra la política de enrutamiento:

`ip rule `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">show|list</span>

- Agrega una nueva regla basada en las direcciones fuente de paquetes:

`sudo ip rule add from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2/32</span>

- Añade una nueva regla basada en direcciones destino de paquetes:

`sudo ip rule add to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2/32</span>

- Elimina una regla basada en las direcciones fuente de paquetes:

`sudo ip rule delete from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2/32</span>

- Elimina una regla basada en las direcciones destino de paquetes:

`sudo ip rule delete to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2/32</span>

- Limpia todas las reglas eliminadas:

`ip rule flush`

- Guarda todas las reglas en un archivo:

`ip rule save > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/reglas_ip.dat</span>

- Restaura todas las reglas desde un archivo:

`ip rule restore < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/reglas_ip.dat</span>
