---
layout: page
title: common/argon2 (español)
description: "Calcula hashes criptográficos Argon2."
content_hash: da4387e9c89ba7a0ce83307dad5926438c7747b7
last_modified_at: 2023-03-02
related_topics:
  - title: English version
    url: /en/common/argon2.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># argon2

Calcula hashes criptográficos Argon2.
Más información: <https://github.com/P-H-C/phc-winner-argon2#command-line-utility>.

- Calcula un hash con una contraseña y un salt con los parámetros por defecto:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contraseña</span>` | argon2 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texto_salt</span>`"`

- Calcula un hash con el algoritmo especificado:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contraseña</span>`" | argon2 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texto_sal</span>`" -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">d|i|id</span>

- Muestra el hash de salida sin información adicional:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contraseña</span>`" | argon2 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texto_sal</span>`" -e`

- Calcula un hash con una cantidad de i[t]eraciones dada, uso de [m]emoria y parámetros de [p]aralelismo dados:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contraseña</span>`" | argon2 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texto_sal</span>`" -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>