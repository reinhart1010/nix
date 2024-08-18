---
layout: page
title: common/aws-accessanalyzer (español)
description: "Analiza y revisa las políticas de recursos para identificar posibles riesgos de seguridad."
content_hash: 55507a9732216235b81733713c1adabbefb41a18
last_modified_at: 2024-08-18
related_topics:
  - title: English version
    url: /en/common/aws-accessanalyzer.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/aws-accessanalyzer.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aws accessanalyzer

Analiza y revisa las políticas de recursos para identificar posibles riesgos de seguridad.
Más información: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/index.html>.

- Crea un nuevo Access Analyzer:

`aws accessanalyzer create-analyzer --analyzer-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_analizador</span>` --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tipo</span>` --tags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">etiquetas</span>

- Elimina un analizador de acceso existente:

`aws accessanalyzer delete-analyzer --analyzer-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analizador_arn</span>

- Obtiene detalles de un analizador de acceso específico:

`aws accessanalyzer get-analyzer --analyzer-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analizador_arn</span>

- Lista todos los analizadores de acceso:

`aws accessanalyzer list-analyzers`

- Actualiza la configuración de un analizador de acceso:

`aws accessanalyzer update-analyzer --analyzer-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analizador_arn</span>` --tags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nuevas_etiquetas</span>

- Crea una nueva regla de archivo de Access Analyzer:

`aws accessanalyzer create-archive-rule --analyzer-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analizador_arn</span>` --rule-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_regla</span>` --filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filtro</span>

- Elimina una regla de archivo de Access Analyzer:

`aws accessanalyzer delete-archive-rule --analyzer-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analizador_arn</span>` --rule-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_regla</span>

- Lista todas las reglas de archivo de Access Analyzer:

`aws accessanalyzer list-archive-rules --analyzer-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analizador_arn</span>
