---
layout: page
title: linux/modprobe (español)
description: "Añade o elimina módulos del núcleo Linux."
content_hash: 50394338a9e100c29211561af40e345be22a94ce
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/modprobe.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/modprobe.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/modprobe.html
    icon: bi bi-globe
tldri18n_status: 2
---
# modprobe

Añade o elimina módulos del núcleo Linux.
Vea también: `kmod`, para otros comandos de gestión de módulos.
Más información: <https://manned.org/modprobe>.

- Finge cargar un módulo en el kernel, pero no lo hace realmente:

`sudo modprobe --dry-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_módulo</span>

- Carga un módulo en el kernel:

`sudo modprobe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_módulo</span>

- Elimina un módulo del núcleo:

`sudo modprobe --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_módulo</span>

- Elimina un módulo y los que dependen de él desde el núcleo:

`sudo modprobe --remove-dependencies `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_módulo</span>

- Muestra las dependencias de un módulo del kernel:

`sudo modprobe --show-depends `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_módulo</span>
