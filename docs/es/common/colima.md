---
layout: page
title: common/colima (español)
description: "Contenedores en tiempo de ejecución para macOS y Linux con una configuración mínima."
content_hash: 9c422e19edcfd0f58a3be72e86f856e399a375a2
last_modified_at: 2024-03-20
related_topics:
  - title: English version
    url: /en/common/colima.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/colima.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># colima

Contenedores en tiempo de ejecución para macOS y Linux con una configuración mínima.
Más información: <https://github.com/abiosoft/colima>.

- Inicia el daemon en segundo plano:

`colima start`

- Crea un archivo de configuración y lo usa:

`colima start --edit`

- Inicia y configura containerd (instala `nerdctl` para usar containerd a través de `nerdctl`):

`colima start --runtime containerd`

- Inicia con Kubernetes (se requiere `kubectl`):

`colima start --kubernetes`

- Personaliza el recuento de CPU, memoria RAM y espacio en disco (en GiB):

`colima start --cpu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número</span>` --memory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">memoria</span>` --disk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">espacio_de_almacenamiento</span>

- Usa Docker a través de Colima (se requiere Docker):

`colima start`

- Lista contenedores con su información y estado:

`colima list`

- Muestra estado de tiempo de ejecución:

`colima status`
