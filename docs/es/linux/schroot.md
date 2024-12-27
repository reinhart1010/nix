---
layout: page
title: linux/schroot (español)
description: "Ejecuta un comando o inicia una interfaz interactiva de comando con un directorio raíz diferente. Más personalizable que `chroot`."
content_hash: 891d9c1c5e302288dd8cf664f34c634fe6b1a39f
last_modified_at: 2024-12-27
related_topics:
  - title: English version
    url: /en/linux/schroot.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/schroot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# schroot

Ejecuta un comando o inicia una interfaz interactiva de comando con un directorio raíz diferente. Más personalizable que `chroot`.
Más información: <https://wiki.debian.org/Schroot>.

- Lista chroots disponibles:

`schroot --list`

- Ejecuta un comando en un chroot específico:

`schroot --chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chroot</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Ejecuta un comando con opciones en un chroot específico:

`schroot --chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chroot</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">opciones_de_comando</span>

- Ejecuta un comando en todos los chroots disponibles:

`schroot --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Inicia una shell interactiva dentro de un chroot específico como usuario específico:

`schroot --chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chroot</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>

- Inicia una nueva sesión (devuelve un identificador único en `stdout`):

`schroot --begin-session --chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chroot</span>

- Se conecta a una sesión existente:

`schroot --run-session --chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_de_sesión</span>

- Finaliza una sesión en curso:

`schroot --end-session --chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_de_sesión</span>
