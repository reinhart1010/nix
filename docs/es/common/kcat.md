---
layout: page
title: common/kcat (español)
description: "Productor Apache Kafka y herramienta de consumo."
content_hash: e9c07e53a5b046362b9a56234bf862cbfb1c5dcf
last_modified_at: 2024-11-18
related_topics:
  - title: English version
    url: /en/common/kcat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/kcat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/kcat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kcat

Productor Apache Kafka y herramienta de consumo.
Más información: <https://github.com/edenhill/kcat>.

- Consume mensajes empezando por el corrimiento (offset) más nuevo:

`kcat -C -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tema</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">intermediarios</span>

- Consume mensajes comenzando con el offset más antiguo y sale después de recibir el último mensaje:

`kcat -C -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tema</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">intermediarios</span>` -o beginning -e`

- Consume mensajes como grupo de consumidores de Kafka:

`kcat -G `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_de_grupo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tema</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">intermediarios</span>

- Publica el mensaje leyendo de `stdin`:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mensaje</span>` | kcat -P -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tema</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">intermediarios</span>

- Publica mensajes leyendo desde un archivo:

`kcat -P -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tema</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">intermediarios</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Lista metadatos para todos los temas e intermediarios:

`kcat -L -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">intermediarios</span>

- Lista metadatos para un tema específico:

`kcat -L -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tema</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">intermediarios</span>

- Obtiene el offset de un tema/partición para un punto específico en el tiempo:

`kcat -Q -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tema</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">partición</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">marca_de_tiempo_unix</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">intermediarios</span>
