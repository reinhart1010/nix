---
layout: page
title: common/git-commit (español)
description: "Realiza commits de los archivos al repositorio."
content_hash: a6c435d32219012a01f0bbdca3d72a7b6a1543d8
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-commit.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-commit.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-commit.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-commit.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-commit.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/git-commit.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-commit.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-commit.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-commit.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-commit.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git commit

Realiza commits de los archivos al repositorio.
Más información: <https://git-scm.com/docs/git-commit>.

- Realiza un commit de los archivos marcados al repositorio con un mensaje:

`git commit -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mensaje</span>`"`

- Realiza un commit de los archivos marcados con un mensaje leído desde un archivo:

`git commit --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_del_mensaje_del_commit</span>

- Marca automáticamente todos los archivos modificados y realiza un commit con un mensaje:

`git commit -a -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mensaje</span>`"`

- Sustituye el último commit con los cambios marcados actualmente, cambiando el hash del commit:

`git commit --amend`

- Realiza un commit para archivos específicos (marcados previamente):

`git commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo2</span>

- Crea un commit, incluso si no hay archivos marcados:

`git commit -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mensaje</span>`" --allow-empty`
