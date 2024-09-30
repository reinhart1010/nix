---
layout: page
title: linux/evtest (español)
description: "Muestra información de los controladores de dispositivos de entrada."
content_hash: db342d1cf2cd27c2976bbd6bd7f7ee245125524b
last_modified_at: 2024-09-30
related_topics:
  - title: English version
    url: /en/linux/evtest.html
    icon: bi bi-globe
tldri18n_status: 2
---
# evtest

Muestra información de los controladores de dispositivos de entrada.
Más información: <https://manned.org/evtest>.

- Lista todos los dispositivos de entrada detectados:

`sudo evtest`

- Muestra los eventos de un dispositivo de entrada específico:

`sudo evtest /dev/input/event`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número</span>

- Agarra el dispositivo exclusivamente, evitando que otros clientes reciban eventos:

`sudo evtest --grab /dev/input/event`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número</span>

- Consulta el estado de una tecla o botón específico en un dispositivo de entrada:

`sudo evtest --query /dev/input/event`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tipo_evento</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">código_evento</span>
