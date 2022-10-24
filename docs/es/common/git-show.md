---
layout: page
title: common/git-show (español)
description: "Muestra varios tipos de objetos Git (commits, etiquetas, etcétera)."
content_hash: abe9e3db2599eee54702def004b0055b834f4afe
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
---
# git show

Muestra varios tipos de objetos Git (commits, etiquetas, etcétera).
Más información: <https://git-scm.com/docs/git-show>.

- Muestra información sobre el último commit (hash, mensaje, cambios y otros metadatos):

`git show`

- Muestra información de un commit específico:

`git show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Muestra información del commit asociado a una determinada etiqueta:

`git show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">etiqueta</span>

- Muestra información del tercer commit desde la punta de una rama:

`git show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rama</span>`~`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- Muestra el mensaje de un commit en una única línea, eliminando el resultado de la diferencia:

`git show --oneline -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Muestra solo estadísticas (caracteres agregados o removidos) de los archivos modificados:

`git show --stat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Muestra solo la lista de archivos agregados, renombrados o eliminados:

`git show --summary `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Muestra el contenido de un archivo en una revisión específica (por ej., una rama, una etiqueta o un commit):

`git show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revisión</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
