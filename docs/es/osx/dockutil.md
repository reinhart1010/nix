---
layout: page
title: osx/dockutil (español)
description: "Gestiona los elementos del dock de macOS."
content_hash: 8afcfbeb27f42eb9207e141944530b099a53cdc1
last_modified_at: 2024-01-26
related_topics:
  - title: English version
    url: /en/osx/dockutil.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/osx/dockutil.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dockutil

Gestiona los elementos del dock de macOS.
Más información: <https://github.com/kcrawford/dockutil>.

- Añade una aplicación al final del dock del usuario actual:

`dockutil --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/aplicación</span>

- Reemplaza una aplicación por otra en el dock del usuario actual:

`dockutil --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/aplicación</span>` --replacing '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">etiqueta_de_elemento_del_dock</span>`'`

- Añade un directorio con opciones de visualización y lo muestra como un icono de carpeta o pila:

`dockutil --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/ruta/al/directorio</span>` --view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grill|fan|list|auto</span>` --display `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">folder|stack</span>

- Añade la URL de un elemento del dock después de otro elemento:

`dockutil --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vnc://ejemplo_servidor.local</span>` --label '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VNC de ejemplo</span>`' --after `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">etiqueta_de_elemento_del_dock</span>

- Elimina una aplicación del dock dado su nombre de etiqueta en el dock:

`dockutil --remove '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">etiqueta_de_elemento_del_dock</span>`'`

- Añade un espaciador en una sección después de una aplicación:

`dockutil --add '' --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">spacer|small-spacer|flex-spacer</span>` --section `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">apps</span>` --after `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">etiqueta_de_elemento_del_dock</span>

- Elimina todos los elementos espaciadores:

`dockutil --remove spacer-tiles`
