---
layout: page
title: linux/scriptlive (español)
description: "Ejecuta un typescript creado por el comando `script` en tiempo real."
content_hash: 53fb3ce95efde2eb742f9ac31c4bd151defd8ca2
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/scriptlive.html
    icon: bi bi-globe
tldri18n_status: 2
---
# scriptlive

Ejecuta un typescript creado por el comando `script` en tiempo real.
Vea también: `script`.
Más información: <https://manned.org/scriptlive>.

- Ejecuta un typescript en tiempo real:

`scriptlive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_tiempo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/typescript</span>

- Ejecuta un typescript al doble de la velocidad original:

`scriptlive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_timing</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/typescript</span>` --divisor 2`

- Ejecuta un guión tipográfico creado con la opción `--log-in` de `script`:

`scriptlive --log-in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_registro</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/typescript</span>

- Ejecuta un typescript esperando como máximo 2 segundos entre cada comando:

`scriptlive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_tiempo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/typescript</span>` --maxdelay 2`
