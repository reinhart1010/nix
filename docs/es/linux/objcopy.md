---
layout: page
title: linux/objcopy (español)
description: "Copia el contenido de un archivo de objetos a otro archivo."
content_hash: 5af453f0c39b04b4ed4f31a2fc6f2c50d57f6143
last_modified_at: 2024-05-12
related_topics:
  - title: English version
    url: /en/linux/objcopy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# objcopy

Copia el contenido de un archivo de objetos a otro archivo.
Más información: <https://manned.org/objcopy>.

- Copia datos a otro archivo:

`objcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_origen</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_destino</span>

- Traduce ficheros de un formato a otro:

`objcopy --input-target=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formato_de_entrada</span>` --output-target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formato_de_salida</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_origen</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_destino</span>

- Elimina toda la información de símbolos del archivo:

`objcopy --strip-all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_origen</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_destino</span>

- Elimina la información de depuración del archivo:

`objcopy --strip-debug `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_origen</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_destino</span>

- Copia una sección específica del archivo de origen al archivo de destino:

`objcopy --only-section `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">section</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_origen</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_destino</span>
