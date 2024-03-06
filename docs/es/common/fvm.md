---
layout: page
title: common/fvm (español)
description: "Gestor de versiones de Flutter."
content_hash: 10e81fe700a0519a2f14d29f71dc21e7ef4c565c
last_modified_at: 2024-03-06
related_topics:
  - title: English version
    url: /en/common/fvm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/fvm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fvm

Gestor de versiones de Flutter.
Más información: <https://fvm.app/documentation/guides/basic-commands>.

- Instala una versión del SDK de Flutter. Invoca el programa sin el argumento `versión` para la configuración del proyecto:

`fvm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versión</span>

- Establece una versión específica del Flutter SDK en un proyecto:

`fvm use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versión</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">opciones</span>

- Establece una versión global del SDK de Flutter:

`fvm global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versión</span>

- Borra la caché de FVM:

`fvm destroy`

- Elimina una versión específica del SDK de Flutter:

`fvm remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versión</span>

- Lista todas las versiones instaladas del SDK de Flutter:

`fvm list`

- Lista todas las versiones del SDK de Flutter:

`fvm releases`
