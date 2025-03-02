---
layout: page
title: common/git-cliff (español)
description: "Un generador de registros de cambios altamente personalizable."
content_hash: aee44c3ffda02c713b8f138649d6fdcbe5bdbf13
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/git-cliff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git cliff

Un generador de registros de cambios altamente personalizable.
Más información: <https://git-cliff.org/docs/usage/args>.

- Genera un registro de cambios a partir de todos los commits de un repositorio Git y lo guarda en `CHANGELOG.md`:

`git cliff > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">CHANGELOG.md</span>

- Genera un registro de cambios a partir de los commits desde la última etiqueta y lo imprime en `stdout`:

`git cliff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|--latest</span>

- Genera un registro de cambios a partir de los commits que pertenecen a la etiqueta actual (usa `git checkout` en una etiqueta anterior a esta):

`git cliff --current`

- Genera un registro de cambios a partir de las confirmaciones que no pertenecen a una etiqueta:

`git cliff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-u|--unreleased</span>

- Escribe el archivo de configuración por defecto en `cliff.toml` en el directorio actual:

`git cliff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--init</span>
