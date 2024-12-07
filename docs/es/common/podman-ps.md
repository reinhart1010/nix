---
layout: page
title: common/podman-ps (español)
description: "Lista los contenedores Podman."
content_hash: 4e40b5fbf8a619773e657cf515abdf0491f985af
last_modified_at: 2024-12-07
related_topics:
  - title: English version
    url: /en/common/podman-ps.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/podman-ps.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/podman-ps.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/podman-ps.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># podman ps

Lista los contenedores Podman.
Más información: <https://docs.podman.io/en/latest/markdown/podman-ps.1.html>.

- Lista los contenedores Podman actualmente en ejecución:

`podman ps`

- Lista todos los contenedores Podman (corriendo y detenidos):

`podman ps --all`

- Muestra el último contenedor creado (incluye todos los estados):

`podman ps --latest`

- Filtra los contenedores que contienen una subcadena en su nombre:

`podman ps --filter "name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>`"`

- Filtra los contenedores que comparten una imagen dada como ancestro:

`podman ps --filter "ancestor=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagen</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">etiqueta</span>`"`

- Filtra por código de estado de salida:

`podman ps --all --filter "exited=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">código</span>`"`

- Filtra los contenedores por estado (created, running, removing, paused, exited y dead). Se usa el término en inglés:

`podman ps --filter "status=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">estado</span>`"`

- Filtra contenedores que montan un volumen específico o tienen un volumen montado en una ruta específica:

`podman ps --filter "volume=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>`" --format "table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.ID</span>`\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Image</span>`\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Names</span>`\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Mounts</span>`"`
