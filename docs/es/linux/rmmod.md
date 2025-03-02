---
layout: page
title: linux/rmmod (español)
description: "Elimina módulos del núcleo Linux."
content_hash: afd488b234076957b53002a05b5c4b7a91f635bf
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/rmmod.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/rmmod.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rmmod

Elimina módulos del núcleo Linux.
Vea también: `kmod`, para otros comandos de gestión de módulos.
Más información: <https://manned.org/rmmod>.

- Elimina un módulo del kernel:

`sudo rmmod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_módulo</span>

- Elimina un módulo del kernel y muestra información detallada:

`sudo rmmod --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_módulo</span>

- Elimina un módulo del kernel y envía los errores a syslog en lugar de a `stderr`:

`sudo rmmod --syslog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_modulo</span>

- Muestra la ayuda:

`rmmod --help`

- Muestra la versión:

`rmmod --version`
