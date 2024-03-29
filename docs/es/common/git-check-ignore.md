---
layout: page
title: common/git-check-ignore (español)
description: "Analiza y depura los archivos que Git debe ignorar / excluir (.gitignore)."
content_hash: b186def0082856b00f6daeb42acc2f328d6a96fe
last_modified_at: 2024-01-07
related_topics:
  - title: English version
    url: /en/common/git-check-ignore.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-check-ignore.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-check-ignore.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-check-ignore.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-check-ignore.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-check-ignore.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git check-ignore

Analiza y depura los archivos que Git debe ignorar / excluir (.gitignore).
Más información: <https://git-scm.com/docs/git-check-ignore>.

- Comprueba si un archivo o directorio es ignorado:

`git check-ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_directorio</span>

- Comprueba si varios archivos o directorios son ignorados:

`git check-ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_directorio1 ruta/al/archivo_o_directorio2 ...</span>

- Usa nombres de rutas, uno por línea, a partir de la entrada estandar (`stdin`):

`git check-ignore --stdin < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_lista</span>

- Comprueba sin leer el índice (se utiliza para depurar por qué las rutas fueron rastreadas y no ignoradas):

`git check-ignore --no-index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_directorio1 ruta/al/archivo_o_directorio2 ...</span>

- Incluye detalles sobre el patrón de coincidencia para cada ruta:

`git check-ignore --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_directorio1 ruta/al/archivo_o_directorio2 ...</span>
