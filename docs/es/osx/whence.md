---
layout: page
title: osx/whence (español)
description: "Un comando integrado de zsh para indicar cómo se interpretaría un comando dado."
content_hash: 27e7aee8f2ee14fc31f1d4be30b7af5208e7c45c
last_modified_at: 2023-08-09
related_topics:
  - title: English version
    url: /en/osx/whence.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># whence

Un comando integrado de zsh para indicar cómo se interpretaría un comando dado.
Más información: <https://www.unix.com/man-page/OpenSolaris/1/whence/>.

- Interpreta `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`, con expansión si se define como un `alias` (similar al `command -v` integrado):

`whence "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`"`

- Muestra tipo de `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`, con localización si se define como una función, o binario (equivalente a los `type` y `command -V` integrados):

`whence -v "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`"`

- Igual que el anterior, excepto que muestra el contenido de las funciones del shell en lugar de la ubicación (equivalente al `which` integrado):

`whence -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`"`

- Igual que el anterior, pero muestra todas las apariciones en la ruta del comando (equivalente al `where` integrado):

`whence -ca "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`"`

- Buscar sólo el `PATH`para `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`, ignorando los buildins, aliases o funciones del shell (equivalente al comando `where`):

`whence -p "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`"`
