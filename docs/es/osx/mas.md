---
layout: page
title: osx/mas (español)
description: "Interfaz de línea de comandos para la Mac App Store."
content_hash: 55ff1e573c176c44510e4f0fee6f64e9df9889c3
last_modified_at: 2023-11-12
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

`mas search " `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aplicación</span>`" --price`

- Instala o actualiza una aplicación:

`mas install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_producto</span>

- Instala todas las actualizaciones pendientes:

`mas upgrade`
