---
layout: page
title: osx/mas (español)
description: "Interfaz de línea de comandos para la Mac App Store."
content_hash: 92823ba4cd360e0e5d9c4dabc3c522c2d32d90d1
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/osx/mas.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/mas.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mas

Interfaz de línea de comandos para la Mac App Store.
Más información: <https://github.com/mas-cli/mas>.

- Inicia sesión en la Mac App Store por primera vez:

`mas signin "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario@ejemplo.com</span>`"`

- Muestra todas las aplicaciones instaladas y sus identificadores de producto:

`mas list`

- Busca una aplicación, mostrando el precio junto a los resultados:

`mas search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aplicación</span>`" --price`

- Instala o actualiza una aplicación utilizando el identificador numérico exacto:

`mas install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_producto_numérico</span>

- Instala la primera aplicación que devuelva la búsqueda correspondiente:

`mas lucky "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">término_de_búsqueda</span>`"`

- Lista todas las aplicaciones obsoletas con actualizaciones pendientes:

`mas outdated`

- Instala todas las actualizaciones pendientes:

`mas upgrade`

- Actualiza una aplicación específica:

`mas upgrade "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_producto_numérico</span>`"`
