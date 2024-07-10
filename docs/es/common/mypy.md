---
layout: page
title: common/mypy (español)
description: "Verificación de código Python."
content_hash: 937b34e749fa0581f322a38873c74e9040801f7f
last_modified_at: 2024-07-10
related_topics:
  - title: English version
    url: /en/common/mypy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mypy

Verificación de código Python.
Más información: <https://mypy.readthedocs.io/en/stable/running_mypy.html>.

- Comprueba un archivo específico:

`mypy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.py</span>

- Comprueba un [m]ódulo específico:

`mypy -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_módulo</span>

- Comprueba un [p]aquete específico:

`mypy -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_paquete</span>

- Comprueba una cadena de código:

`mypy -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">código</span>`"`

- Ignora importaciones faltantes:

`mypy --ignore-missing-imports `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al_archivo_o_directorio</span>

- Muestra mensajes de error detallados:

`mypy --show-traceback `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_directorio</span>

- Especifica un archivo de configuración personalizado:

`mypy --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_configuración</span>

- Muestra ayuda:

`mypy -h`
