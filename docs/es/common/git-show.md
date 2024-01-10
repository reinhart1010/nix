---
layout: page
title: common/git-show (español)
description: "Muestra varios tipos de objetos Git (confirmaciones, etiquetas, etcétera)."
content_hash: 4d0fd79de03b1f5656657933a24117e01efd0159
last_modified_at: 2024-01-10
related_topics:
  - title: English version
    url: /en/common/git-show.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-show.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-show.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-show.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git show

Muestra varios tipos de objetos Git (confirmaciones, etiquetas, etcétera).
Más información: <https://git-scm.com/docs/git-show>.

- Muestra información sobre la última confirmación (hash, mensaje, cambios y otros metadatos):

`git show`

- Muestra información de una confirmación específica:

`git show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">confirmación</span>

- Muestra información de la confirmación asociada a una determinada etiqueta:

`git show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">etiqueta</span>

- Muestra información de la tercera confirmación desde la punta de una rama:

`git show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rama</span>`~`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- Muestra el mensaje de una confirmación en una única línea, eliminando el resultado de la diferencia:

`git show --oneline -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">confirmación</span>

- Muestra solo estadísticas (caracteres agregados o removidos) de los archivos modificados:

`git show --stat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">confirmación</span>

- Muestra solo la lista de archivos agregados, renombrados o eliminados:

`git show --summary `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">confirmación</span>

- Muestra el contenido de un archivo en una revisión específica (por ej., una rama, una etiqueta o una confirmación):

`git show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revisión</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
