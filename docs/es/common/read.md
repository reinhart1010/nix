---
layout: page
title: common/read (español)
description: "Shell builtin para recuperar datos de `stdin`."
content_hash: 91d8af7cf02bbeb33b655feb3fb3be1a753dacb8
last_modified_at: 2024-12-05
related_topics:
  - title: English version
    url: /en/common/read.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/read.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/read.html
    icon: bi bi-globe
tldri18n_status: 2
---
# read

Shell builtin para recuperar datos de `stdin`.
Más información: <https://manned.org/read.1p>.

- Almacena los datos que escribes desde el teclado:

`read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>

- Almacena cada una de las siguientes líneas que introduzcas como valores de un arreglo:

`read -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arreglo</span>

- Especifica el número máximo de caracteres a leer:

`read -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cuenta_caracteres</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>

- Asigna varios valores a varias variables:

`read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">_ variable1 _ variable2</span>` <<< "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">El apellido es Bond"</span>`"`

- No dejes que la barra invertida (\) actúe como carácter de escape:

`read -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>

- Muestra un indicador antes de la entrada:

`read -p "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Introduce aquí tu entrada: </span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>

- No hacer eco de los caracteres introducidos (modo silencioso):

`read -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>

- Lee `stdin` y realiza una acción en cada línea:

`while read line; do `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo|ls|rm|...</span>` "$line"; done < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dev/stdin|ruta/al/archivo|...</span>
