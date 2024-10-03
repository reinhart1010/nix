---
layout: page
title: common/dotenvx (español)
description: "Un `dotenv` mejor, del creador de `dotenv`."
content_hash: 2a1a33a83ec99733ccc4a6a7aa8ff2e016e1b81f
last_modified_at: 2024-10-03
related_topics:
  - title: English version
    url: /en/common/dotenvx.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dotenvx

Un `dotenv` mejor, del creador de `dotenv`.
Más información: <https://dotenvx.com/docs>.

- Ejecuta un comando con variables de entorno desde un archivo `.env`:

`dotenvx run -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Ejecuta un comando con variables de entorno desde un archivo `.env` específico:

`dotenvx run -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.env</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Establece una variable de entorno con cifrado:

`dotenvx set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clave</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>

- Establece una variable de entorno sin encriptación:

`dotenvx set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clave</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>` --plain`

- Devuelve las variables de entorno definidas en un archivo `.env`:

`dotenvx get`

- Devuelve el valor de una variable de entorno definida en un archivo `.env`:

`dotenvx get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clave</span>

- Devuelve todas las variables de entorno de los archivos `.env` y OS:

`dotenvx get --all`
