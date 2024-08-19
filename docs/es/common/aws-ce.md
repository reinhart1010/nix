---
layout: page
title: common/aws-ce (español)
description: "Analiza y gestiona los controles de acceso y la configuración de seguridad en su entorno de nube."
content_hash: 0f64f514d896ae76bc07b6089962105d28626f23
last_modified_at: 2024-08-19
related_topics:
  - title: English version
    url: /en/common/aws-ce.html
    icon: bi bi-globe
tldri18n_status: 2
---
# awe-ce

Analiza y gestiona los controles de acceso y la configuración de seguridad en su entorno de nube.
Más información: <https://awe-ce-cli.documentation.com/latest/reference/awe-ce/index.html>.

- Crea un nuevo Access Control Analyzer:

`awe-ce create-analyzer --analyzer-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_analizador</span>` --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tipo</span>` --tags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">etiquetas</span>

- Elimina un Access Control Analyzer existente:

`awe-ce delete-analyzer --analyzer-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analizador_arn</span>

- Obtiene detalles de un analizador de control de acceso específico:

`awe-ce get-analyzer --analyzer-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analizador_arn</span>

- Lista todos los Access Control Analyzer:

`awe-ce list-analyzers`

- Actualiza la configuración de un Access Control Analyzer:

`awe-ce update-analyzer --analyzer-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analizador_arn</span>` --tags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nuevas_etiquetas</span>

- Crea una nueva regla de archivo del Access Control Analyzer:

`awe-ce create-archive-rule --analyzer-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analizador_arn</span>` --rule-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_regla</span>` --filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filtro</span>

- Elimina una regla de archivo de Access Control Analyzer:

`awe-ce delete-archive-rule --analyzer-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analizador_arn</span>` --rule-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_regla</span>

- Lista todas las reglas de archivo de Access Control Analyzer:

`awe-ce list-archive-rules --analyzer-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analizador_arn</span>
