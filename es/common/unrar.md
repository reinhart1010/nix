---
layout: page
title: common/unrar (español)
description: "Extrae archivos RAR."
content_hash: 435f3e1966d03b30754a67ad98f1df9466b9b4c0
related_topics:
  - title: English version
    url: /en/common/unrar.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/unrar.html
    icon: bi bi-globe
---
# unrar

Extrae archivos RAR.

- Extrae archivos comprimidos respetando la estructura original del archivo:

`unrar x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_comprimido.rar</span>

- Extrae archivos comprimidos en una ruta determinada respetando la estructura original del archivo:

`unrar x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_comprimido.rar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/donde/extraer</span>

- Extrae archivos comprimidos en el directorio actual, perdiendo la estructura original del archivo:

`unrar e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_comprimido.rar</span>

- Comprueba la integridad de cada uno de los archivos dentro del archivo comprimido:

`unrar t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_comprimido.rar</span>

- Muestra el listado de los archivos dentro del archivo comprimido sin descomprimirlo:

`unrar l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_comprimido.rar</span>
