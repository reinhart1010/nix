---
layout: page
title: common/podman-rmi (español)
description: "Elimina imágenes de Podman."
content_hash: 43a8f6dc33e2483fa0582615602b94f9a4ef4d8e
last_modified_at: 2024-12-08
related_topics:
  - title: English version
    url: /en/common/podman-rmi.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/podman-rmi.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/podman-rmi.html
    icon: bi bi-globe
tldri18n_status: 2
---
# podman rmi

Elimina imágenes de Podman.
Más información: <https://docs.podman.io/en/latest/markdown/podman-rmi.1.html>.

- Elimina una o más imágenes dados sus nombres:

`podman rmi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagen:tag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagen2:tag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">...</span>

- Fuerza eliminar una imagen:

`podman rmi --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagen</span>

- Quita una imagen sin eliminar padres sin etiquetar:

`podman rmi --no-prune `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">imagen</span>

- Muestra ayuda:

`podman rmi`
