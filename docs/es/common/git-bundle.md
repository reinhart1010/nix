---
layout: page
title: common/git-bundle (español)
description: "Empaqueta objetos y referencias en un archivo."
content_hash: b0efb4fdfdc672b2b8ff2bac9ee7e5e59c3b5835
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/git-bundle.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-bundle.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-bundle.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-bundle.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-bundle.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-bundle.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-bundle.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git bundle

Empaqueta objetos y referencias en un archivo.
Más información: <https://git-scm.com/docs/git-bundle>.

- Crea un archivo bundle que contiene todos los objetos y referencias de una rama específica:

`git bundle create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.bundle</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_rama</span>

- Crea un archivo bundle de todas las ramas:

`git bundle create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.bundle</span>` --all`

- Crea un archivo bundle de los últimos 5 commits de la rama actual:

`git bundle create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.bundle</span>` -5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Crea un archivo bundle de los últimos 7 días:

`git bundle create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.bundle</span>` --since 7.days `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Verifica que un archivo bundle es válido y puede aplicarse al repositorio actual:

`git bundle verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.bundle</span>

- Imprime en `stdout` la lista de referencias contenidas en un bundle:

`git bundle unbundle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.bundle</span>

- Desagrupa una rama específica de un archivo bundle en el repositorio actual:

`git pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.bundle</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_rama</span>

- Crea un nuevo repositorio a partir de un paquete:

`git clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.bundle</span>
