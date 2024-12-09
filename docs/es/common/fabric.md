---
layout: page
title: common/fabric (español)
description: "Un marco de trabajo de código abierto para aumentar el número de humanos utilizando IA."
content_hash: 083d41697ab80b9c0295c17e56cc645a0dbf63c2
last_modified_at: 2024-12-09
related_topics:
  - title: English version
    url: /en/common/fabric.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fabric

Un marco de trabajo de código abierto para aumentar el número de humanos utilizando IA.
Proporciona un marco modular para resolver problemas específicos utilizando un conjunto de instrucciones de IA de origen colectivo.
Más información: <https://github.com/danielmiessler/fabric>.

- Ejecuta el setup para configurar fabric:

`fabric --setup`

- Lista todos los patrones disponibles:

`fabric --listpatterns`

- Ejecuta un patrón con la entrada de un archivo:

`fabric --pattern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_patrón</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_entrada</span>

- Ejecuta un patrón en la URL de un vídeo de YouTube:

`fabric --youtube "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.youtube.com/watch?v=id_del_video</span>`" --pattern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_patrón</span>

- Encadena patrones pasando la salida de uno a otro:

`fabric --pattern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón1</span>` | fabric --pattern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón2</span>

- Ejecuta un patrón personalizado definido por el usuario:

`fabric --pattern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_patrón_personalizado</span>

- Ejecuta un patrón y guarda el resultado en un archivo:

`fabric --pattern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_patrón</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo_salida</span>

- Ejecuta un patrón con las variables especificadas:

`fabric --pattern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_patrón</span>` --variable "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_variable</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>`"`
