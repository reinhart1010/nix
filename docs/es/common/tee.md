---
layout: page
title: common/tee (español)
description: "Lee desde la entrada estándar y escribe a la salida estándar a la vez que a archivos o comandos."
content_hash: f6681c6eece338bec7573648bb669a4f9e3a9248
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/tee.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># tee

Lee desde la entrada estándar y escribe a la salida estándar a la vez que a archivos o comandos.
Más información: <https://www.gnu.org/software/coreutils/tee>.

- Copia la entrada estándar al archivo, reemplazando su contenido, y también a la salida estándar:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ejemplo</span>` | tee `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Anexa la entrada estándar al archivo, sin reemplazar:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ejemplo</span>` | tee -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Imprime la entrada estándar a la terminal, y también lo reenvía a otro programa para posterior procesamiento:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ejemplo</span>` | tee `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/tty</span>` | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xargs printf "[%s]"</span>
