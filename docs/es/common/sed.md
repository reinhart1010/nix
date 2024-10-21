---
layout: page
title: common/sed (español)
description: "Edita texto de manera scriptable."
content_hash: 19693ca4fdf0421352e5351cc463e3a469a97e88
last_modified_at: 2024-10-21
related_topics:
  - title: dansk version
    url: /da/common/sed.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/sed.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/sed.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/sed.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/sed.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sed

Edita texto de manera scriptable.
Vea también: `awk`, `ed`.
Más información: <https://manned.org/sed.1posix>.

- Reemplaza todas las ocurrencias de `apple` (regex básica) por `mango` (regex básica) en todas las líneas de entrada y muestra el resultado en `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | sed 's/apple/mango/g'`

- Ejecuta un archivo de script específico y muestra el resultado en `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | sed -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/script.sed</span>

- Imprime solo la primera línea en `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | sed -n '1p'`
