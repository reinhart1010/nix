---
layout: page
title: osx/spctl (español)
description: "Gestiona el subsistema de políticas de evaluación de seguridad."
content_hash: 928184807dddf4494286b5b6916feb38993fd05f
last_modified_at: 2024-02-04
related_topics:
  - title: English version
    url: /en/osx/spctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# spctl

Gestiona el subsistema de políticas de evaluación de seguridad.
Utilidad para gestionar Gatekeeper en macOS.
Más información: <https://keith.github.io/xcode-man-pages/spctl.8.html>.

- Desactiva Gatekeeper:

`spctl --master-disable`

- Añade una regla para permitir la ejecución de una aplicación (el etiquetado de la regla es opcional):

`spctl --add --label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_regla</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Activa Gatekeeper:

`spctl --master-enable`

- Lista todas las reglas del sistema:

`spctl --list`
