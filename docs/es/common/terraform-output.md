---
layout: page
title: common/terraform-output (español)
description: "Exporta datos estructurados sobre tus recursos Terraform."
content_hash: e3d48be7131504126c83a86c7c3a2bc2740977d8
last_modified_at: 2024-08-04
related_topics:
  - title: English version
    url: /en/common/terraform-output.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/terraform-output.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># terraform output

Exporta datos estructurados sobre tus recursos Terraform.
Más información: <https://developer.hashicorp.com/terraform/cli/commands/output>.

- Sin argumentos adicionales, `output` mostrará todas las salidas del módulo raíz:

`terraform output`

- Genera solo un valor con un nombre específico:

`terraform output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>

- Convierte el valor de salida en una cadena sin formato (útil para scripts de shell):

`terraform output -raw`

- Formatea las salidas como un objeto JSON, con una clave por cada salida (útil con jq):

`terraform output -json`
