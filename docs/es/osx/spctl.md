---
layout: page
title: osx/spctl (español)
description: "Gestiona el subsistema de políticas de evaluación de seguridad."
content_hash: bf158bb4365cad350f368ac1c4c3eb874969d947
last_modified_at: 2023-07-08
related_topics:
  - title: English version
    url: /en/osx/spctl.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># spctl

Gestiona el subsistema de políticas de evaluación de seguridad.
Utilidad para gestionar Gatekeeper en macOS.
Más información: <https://www.unix.com/man-page/osx/8/SPCTL/>.

- Desactiva Gatekeeper:

`spctl --master-disable`

- Añade una regla para permitir la ejecución de una aplicación (el etiquetado de la regla es opcional):

`spctl --add --label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_regla</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Activa Gatekeeper:

`spctl --master-enable`

- Lista todas las reglas del sistema:

`spctl --list`
