---
layout: page
title: osx/whence (español)
description: "Un comando integrado de zsh para indicar cómo se interpretaría un comando dado."
content_hash: e419c8f3f06e9e5ef4fd41080f42c7cfbd25be8c
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/whence.html
    icon: bi bi-globe
tldri18n_status: 2
---
# whence

Un comando integrado de zsh para indicar cómo se interpretaría un comando dado.
Más información: <https://www.unix.com/man-page/OpenSolaris/1/whence/>.

- Interpreta `comando`, con expansión si se define como un `alias` (similar al `command -v` integrado):

`whence "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`"`

- Muestra tipo de `comando`, con localización si se define como una función, o binario (equivalente a los `type` y `command -V` integrados):

`whence -v "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`"`

- Igual que el anterior, excepto que muestra el contenido de las funciones del shell en lugar de la ubicación (equivalente al `which` integrado):

`whence -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`"`

- Igual que el anterior, pero muestra todas las apariciones en la ruta del comando (equivalente al `where` integrado):

`whence -ca "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`"`

- Buscar sólo el `PATH` para `comando`, ignorando los buildins, aliases o funciones del shell (equivalente al comando `where`):

`whence -p "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`"`
