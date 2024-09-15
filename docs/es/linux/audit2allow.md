---
layout: page
title: linux/audit2allow (español)
description: "Crea un módulo de política local SELinux para permitir reglas basadas en operaciones denegadas encontradas en los logs."
content_hash: 8f79196c87ac6187f808331f8ccd21a46112ea25
last_modified_at: 2024-09-15
related_topics:
  - title: English version
    url: /en/linux/audit2allow.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/audit2allow.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># audit2allow

Crea un módulo de política local SELinux para permitir reglas basadas en operaciones denegadas encontradas en los logs.
Nota: Utiliza audit2allow con precaución - revisa siempre la directiva generada antes de aplicarla, ya que puede permitir un acceso excesivo.
Más información: <https://manned.org/audit2allow>.

- Genera una política local para permitir el acceso a todos los servicios denegados:

`sudo audit2allow --all -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_normativa_local</span>

- Genera un módulo de normativa local para conceder acceso a un proceso/servicio/comando específico de los registros de auditoría:

`sudo grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">apache2</span>` /var/log/audit/audit.log | sudo audit2allow -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_normativa_local</span>

- Inspecciona y revisa el archivo Type Enforcement (.te) para una normativa local:

`vim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_normativa_local</span>`.te`

- Instala un módulo de normativa local:

`sudo semodule -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_normativa_local</span>`.pp`
