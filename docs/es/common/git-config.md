---
layout: page
title: common/git-config (español)
description: "Gestiona opciones de configuración personalizadas para repositorios Git."
content_hash: 66ef5fa597f7bb2568ae35d2f860e4c83ed6516b
last_modified_at: 2024-08-24
related_topics:
  - title: Deutsch version
    url: /de/common/git-config.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-config.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-config.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-config.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-config.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-config.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-config.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-config.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-config.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-config.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git config

Gestiona opciones de configuración personalizadas para repositorios Git.
Estas configuraciones pueden ser locales (para el repositorio actual) o globales (para el usuario actual).
Más información: <https://git-scm.com/docs/git-config>.

- Establece globalmente tu nombre o correo electrónico (esta información es necesaria para hacer un commit en un repositorio y se incluirá en todos los commits):

`git config --global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user.name|user.email</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Tu nombre|email@example.com</span>`"`

- Lista las entradas de configuración local o global:

`git config --list --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local|global</span>

- Lista sólo las entradas de configuración del sistema (almacenadas en `/etc/gitconfig`), y muestra la ubicación de dicho archivo:

`git config --list --system --show-origin`

- Obtén el valor de una entrada de configuración dada:

`git config alias.unstage`

- Establece el valor global de una entrada de configuración dada:

`git config --global alias.unstage "reset HEAD --"`

- Revierte una entrada de configuración global a su valor por defecto:

`git config --global --unset alias.unstage`

- Edita la configuración local de Git (`.git/config`) en el editor por defecto:

`git config --edit`

- Edita la configuración global de Git (`~/.gitconfig` por defecto o `$XDG_CONFIG_HOME/git/config` si existe tal archivo) en el editor por defecto:

`git config --global --edit`
