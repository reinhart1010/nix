---
layout: page
title: common/podman-machine (español)
description: "Crea y gestiona máquinas virtuales ejecutando Podman."
content_hash: e9b3e636082e2575a53236ba5f2b7c872963302a
last_modified_at: 2024-12-07
related_topics:
  - title: English version
    url: /en/common/podman-machine.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/podman-machine.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/podman-machine.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/podman-machine.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># podman machine

Crea y gestiona máquinas virtuales ejecutando Podman.
Desde la versión 4 o superior de Podman.
Más información: <https://docs.podman.io/en/latest/markdown/podman-machine.1.html>.

- Lista máquinas existentes:

`podman machine ls`

- Crea una nueva máquina predeterminada:

`podman machine init`

- Crea una nueva máquina con un nombre específico:

`podman machine init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>

- Crea una nueva máquina con diferentes recursos:

`podman machine init --cpus=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` --memory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4096</span>` --disk-size=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>

- Inicia o detiene una máquina:

`podman machine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>

- Conecta a una máquina en ejecución a través de SSH:

`podman machine ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>

- Inspecciona información sobre una máquina:

`podman machine inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>
