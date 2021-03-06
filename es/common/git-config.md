---
layout: page
title: common/git-config (español)
description: "Gestiona opciones personalizadas para la configuración de repositorios Git."
content_hash: a7d19b4243a1e1f48265a0b52abe4db15080625c
related_topics:
  - title: English version
    url: /en/common/git-config.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-config.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-config.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-config.html
    icon: bi bi-globe
---
# git config

Gestiona opciones personalizadas para la configuración de repositorios Git.
Estas configuraciones pueden ser locales (para el repositorio actual) o globales (para el usuario actual).
Más información: <https://git-scm.com/docs/git-config>.

- Muestra solo las entradas de la configuración local (almacenadas en `.git/config` en el repositorio actual):

`git config --list --local`

- Muestra solo las entradas de la configuración global (almacenadas en `~/.gitconfig`):

`git config --list --global`

- Muestra todas las entradas de configuración que han sido definidas local o globalmente:

`git config --list`

- Muestra el valor de una entrada específica de la configuración:

`git config alias.unstage`

- Establece el valor global para una entrada específica de la configuración:

`git config --global alias.unstage "reset HEAD --"`

- Revierte una entrada de la configuración global a su valor por defecto:

`git config --global --unset alias.unstage`

- Edita la configuración de Git para el repositorio actual en el editor por defecto:

`git config --edit`

- Edita la configuración global de Git en el editor por defecto:

`git config --global --edit`
