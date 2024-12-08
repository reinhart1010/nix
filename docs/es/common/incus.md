---
layout: page
title: common/incus (español)
description: "Contenedor de sistemas y gestor de máquinas virtuales moderno, seguro y potente."
content_hash: 16bc29be0a24f206871b62e67b95f502f0bbb33f
last_modified_at: 2024-12-08
related_topics:
  - title: English version
    url: /en/common/incus.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/incus.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># incus

Contenedor de sistemas y gestor de máquinas virtuales moderno, seguro y potente.
Más información: <https://linuxcontainers.org/incus/docs/main>.

- Lista todos los contenedores y máquinas virtuales (tanto en ejecución como detenidas):

`incus list`

- Crea un contenedor a partir de una imagen, con un nombre personalizado:

`incus create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagen</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_contenedor</span>

- Inicia o detiene un contenedor existente:

`incus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_contenedor</span>

- Abre un intérprete de comandos dentro de un contenedor en ejecución:

`incus shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_contenedor</span>

- Elimina un contenedor detenido:

`incus delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_contenedor</span>

- Extrae una imagen de un repositorio de imágenes (remoto) al local:

`incus copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remoto</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagen</span>` local:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_imagen_personalizada</span>

- Lista todas las imágenes disponibles en el repositorio oficial `images:` remoto:

`incus image list images:`

- Lista todas las imágenes ya descargadas en el remoto `local:`:

`incus image list local:`
