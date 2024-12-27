---
layout: page
title: common/ruff-check (español)
description: "Un linter extremadamente rápido para Python. `check` es el comando predeterminado - se puede omitir en todas partes."
content_hash: 5ed6df2bfe955f88d6e6d88dba54cceb40e836a1
last_modified_at: 2024-12-27
related_topics:
  - title: English version
    url: /en/common/ruff-check.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ruff-check.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ruff-check.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ruff check

Un linter extremadamente rápido para Python. `check` es el comando predeterminado - se puede omitir en todas partes.
Si no se especifican archivos o directorios, el directorio de trabajo actual se utiliza por defecto.
Más información: <https://docs.astral.sh/ruff/linter>.

- Ejecuta el linter en los archivos o directorios dados:

`ruff check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_directorio1 ruta/al/archivo_o_directorio2 ...</span>

- Aplica las correcciones sugeridas, modificando los archivos afectados:

`ruff check --fix`

- Ejecuta el linter y lo aplica de nuevo ante algún cambio:

`ruff check --watch`

- Solo habilita las reglas especificadas (o todas las reglas), ignorando el archivo de configuración:

`ruff check --select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ALL|regla_de_código1,regla_de_código2,...</span>

- Además, habilita las reglas especificadas:

`ruff check --extend-select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regla_de_código1,regla_de_código2,...</span>

- Desactiva las reglas especificadas:

`ruff check --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regla_de_código1,regla_de_código2,...</span>

- Ignora todas las violaciones existentes de una regla añadiendo las directivas "# noqa" a todas las líneas que la violan:

`ruff check --select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regla_de_código</span>` --add-noqa`
