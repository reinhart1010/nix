---
layout: page
title: osx/whence (español)
description: "Un comando integrado de zsh para indicar cómo se interpretaría un comando dado."
content_hash: 92724cf90174467688255788bc2ad02504bf4264
last_modified_at: 2024-01-07
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

- Busca un comando en la variable de entorno `PATH`, ignorando los comandos integrados, aliases o funciones del shell (equivalente al comando `where`):

`whence -p "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`"`
