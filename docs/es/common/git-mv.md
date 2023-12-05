---
layout: page
title: common/git-mv (español)
description: "Mueve o renombra archivos y actualiza el índice Git."
content_hash: bc616f509dc5ed4e576604c1301a6061e8d46962
last_modified_at: 2023-12-05
related_topics:
  - title: English version
    url: /en/common/git-mv.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-mv.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-mv.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-mv.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-mv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git mv

Mueve o renombra archivos y actualiza el índice Git.
Más información: <https://git-scm.com/docs/git-mv>.

- Mueve el archivo dentro del repositorio y añade el movimiento al siguiente commit:

`git mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nueva/ruta/al/archivo</span>

- Renombra un archivo y añade el renombre al siguiente commit:

`git mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_archivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nuevo_nombre_de_archivo</span>

- Sobrescribe el archivo en la ruta objetivo si existe:

`git mv --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">objetivo</span>
