---
layout: page
title: common/limactl (español)
description: "Administrador de máquinas virtuales para huéspedes Linux, con múltiples plantillas para MV (Máquinas virtuales) disponibles."
content_hash: da1c9cd115f62d213f162100b7c9b349ce36b5fb
last_modified_at: 2024-11-18
related_topics:
  - title: English version
    url: /en/common/limactl.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/limactl.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/limactl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# limactl

Administrador de máquinas virtuales para huéspedes Linux, con múltiples plantillas para MV (Máquinas virtuales) disponibles.
Se puede utilizar para ejecutar contenedores en macOS, pero también para casos de uso genéricos de máquinas virtuales en anfitriones macOS y Linux.
Más información: <https://github.com/lima-vm/lima>.

- Lista MVs (Máquinas virtuales):

`limactl list`

- Crea una MV usando la configuración predeterminada y opcionalmente proporciona un nombre y/o una plantilla (vea `limactl create --list-templates` para plantillas disponibles):

`limactl create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_mv</span>` template://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">debian|fedora|ubuntu|…</span>

- Inicia una MV (esto puede instalar algunas dependencias en la misma y tomar unos minutos):

`limactl start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_mv</span>

- Abre un intérprete de comandos dentro de una MV:

`limactl shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_mv</span>

- Ejecuta un comando dentro de una MV:

`limactl shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_mv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Detiene/apaga una MV:

`limactl stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_mv</span>

- Suprime una MV:

`limactl remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_mv</span>
