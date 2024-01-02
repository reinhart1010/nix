---
layout: page
title: common/git-clone (español)
description: "Clona un repositorio existente."
content_hash: c57950b0da827a902e463f54c6ae38de99b8abc6
last_modified_at: 2024-01-02
related_topics:
  - title: Deutsch version
    url: /de/common/git-clone.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-clone.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-clone.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-clone.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-clone.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-clone.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-clone.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-clone.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-clone.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-clone.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-clone.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git clone

Clona un repositorio existente.
Más información: <https://git-scm.com/docs/git-clone>.

- Clona un repositorio existente en un directorio nuevo (el directorio por defecto es el nombre del repositorio):

`git clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ubicación_repositorio_remoto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Clona un repositorio existente y sus submódulos:

`git clone --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ubicación_repositorio_remoto</span>

- Clona sólo el directorio `.git` de un repositorio existente:

`git clone --no-checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ubicación_repositorio_remoto</span>

- Clona un repositorio local:

`git clone --local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/repositorio/local</span>

- Clona en silencio:

`git clone --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ubicación_repositorio_remoto</span>

- Clona un repositorio existente obteniendo sólo los 10 commits más recientes de la rama por defecto (útil para ahorrar tiempo):

`git clone --depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ubicación_repositorio_remoto</span>

- Clona un repositorio existente buscando sólo una rama específica:

`git clone --branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` --single-branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ubicación_repositorio_remoto</span>

- Clona un repositorio existente usando un comando SSH específico:

`git clone --config core.sshCommand="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssh -i ruta/a/clave_privada_ssh</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ubicación_repositorio_remoto</span>
