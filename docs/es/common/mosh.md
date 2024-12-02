---
layout: page
title: common/mosh (español)
description: "Mobile Shell (`mosh`) es un reemplazo robusto y receptivo para SSH."
content_hash: 175a8dd7029c09b15fe447fc720cc8ab6f016db8
last_modified_at: 2024-12-02
related_topics:
  - title: English version
    url: /en/common/mosh.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/mosh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mosh

Mobile Shell (`mosh`) es un reemplazo robusto y receptivo para SSH.
`mosh` persiste las conexiones con servidores remotos mientras deambula en las redes.
Más información: <https://mosh.org>.

- Conecta a un servidor remoto:

`mosh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">equipo_remoto</span>

- Conecta a un servidor remoto con una identidad específica (clave privada):

`mosh --ssh="ssh -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo_de_clave</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">equipo_remoto</span>

- Conecta a un servidor remoto usando un puerto específico:

`mosh --ssh="ssh -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2222</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">equipo_remoto</span>

- Ejecuta un comando en un servidor remoto:

`mosh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">equipo_remoto</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando -con --opciones</span>

- Selecciona un puerto UDP Mosh (útil cuando el `equipo_remoto` está tras un NAT):

`mosh -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">124</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">equipo_remoto</span>

- Se lo usa cuando el binario `mosh-server` no se encuentra en la ruta estándar:

`mosh --server=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/bin/</span>`mosh-server `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">equipo_remoto</span>
