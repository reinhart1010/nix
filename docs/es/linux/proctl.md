---
layout: page
title: linux/proctl (español)
description: "Gestiona licencias de proyectos e idiomas, cambiar entre licencias de plantillas."
content_hash: f0116679ca9fac2ec23f8c8aaf7aa4c6a1da466a
last_modified_at: 2024-09-12
related_topics:
  - title: English version
    url: /en/linux/proctl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/proctl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># proctl

Gestiona licencias de proyectos e idiomas, cambiar entre licencias de plantillas.
Más información: <https://github.com/HeCodes2Much/proctl>.

- Lista licencias disponibles:

`proctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-ll|-list-licenses</span>

- Lista de idiomas disponibles:

`proctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-lL|-lista-idiomas</span>

- Selecciona una licencia en un menú FZF:

`proctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-pl|-elegir-licencia</span>

- Selecciona un idioma en un menú FZF:

`proctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-pL|-elegir-idioma</span>

- Elimina todas las licencias del proyecto actual:

`proctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|-quitar-licencia</span>

- Crea una nueva plantilla de licencia:

`proctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|-nueva-plantilla</span>

- Elimina una licencia de las plantillas:

`proctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-R|-elimina-licencia</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@nombre_licencia1 @nombre_licencia2 ...</span>

- Muestra esta lista de comandos:

`proctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|-ayuda</span>
