---
layout: page
title: common/pydocstyle (español)
description: "Comprueba estáticamente que los scripts de Python cumplen con las convenciones de documentación de Python."
content_hash: 5fd306ac72490be2fb447c124277c7a5f535dc1c
last_modified_at: 2024-04-03
related_topics:
  - title: English version
    url: /en/common/pydocstyle.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pydocstyle

Comprueba estáticamente que los scripts de Python cumplen con las convenciones de documentación de Python.
Más información: <https://www.pydocstyle.org/en/latest/>.

- Analiza un script de Python o todos los scripts de Python en un directorio específico:

`pydocstyle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo.py|ruta/al/directorio</span>

- Muestra una [e]xplicación de cada error:

`pydocstyle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-e|--explain</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo.py|ruta/al/directorio</span>

- Muestra información de [d]epuración:

`pydocstyle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--debug</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo.py|ruta/al/directorio</span>

- Muestra el número total de errores:

`pydocstyle --count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo.py|ruta/a/directorio</span>

- Utiliza un archivo de configuración específico:

`pydocstyle --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo_config</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo.py|ruta/al/directorio</span>

- Ignora uno o más errores:

`pydocstyle --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">D101,D2,D107,...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo.py|ruta/al/directorio</span>

- Busca errores de una convención específica:

`pydocstyle --convention `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pep257|numpy|google</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo.py|ruta/a/directorio</span>
