---
layout: page
title: common/tee (español)
description: "Lee desde la entrada estándar (`stdin`) y escribe a la salida estándar (`stdout`) y a archivos (o comandos)."
content_hash: 4b8b818783bfe8fc20bafdd584ab7d3d33ef8912
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/tee.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/tee.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/tee.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/tee.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tee

Lee desde la entrada estándar (`stdin`) y escribe a la salida estándar (`stdout`) y a archivos (o comandos).
Más información: <https://www.gnu.org/software/coreutils/manual/html_node/tee-invocation.html>.

- Copia la entrada estándar (`stdin`) a cada archivo, y también a la salida estándar (`stdout`):

`echo "ejemplo" | tee `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Anexa a los archivos específicos, sin sobreescribir:

`echo "ejemplo" | tee -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Imprime la entrada estándar a la terminal, y también lo reenvía a otro programa para posterior procesamiento:

`echo "ejemplo" | tee `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/tty</span>` | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xargs printf "[%s]"</span>

- Crea un directorio llamado "ejemplo", cuenta el número de caracteres en "ejemplo" y escribe "ejemplo" a la terminal:

`echo "ejemplo" | tee >(xargs mkdir) >(wc -c)`
