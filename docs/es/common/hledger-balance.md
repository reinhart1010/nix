---
layout: page
title: common/hledger-balance (español)
description: "Un informe \"sumatorio\" flexible y de propósito general que muestra cuentas con algún tipo de dato numérico."
content_hash: 76ac06e8bad0429d59dfc63e5aee9fe7f417600c
last_modified_at: 2024-06-08
related_topics:
  - title: English version
    url: /en/common/hledger-balance.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/hledger-balance.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># hledger balance

Un informe "sumatorio" flexible y de propósito general que muestra cuentas con algún tipo de dato numérico.
Puede tratarse de cambios de saldo por periodo, saldos finales, rendimiento presupuestario, plusvalías latentes, etc.
Más información: <https://hledger.org/hledger.html#balance>.

- Muestra el cambio de saldo en todas las cuentas de todas las contabilizaciones a lo largo de todo el tiempo:

`hledger balance`

- Muestra el cambio de saldo en las cuentas denominadas `*gastos*`, como un árbol, resumiendo solo los dos niveles superiores:

`hledger balance `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gastos</span>` --tree --depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>

- Muestra los gastos de cada mes, y sus totales y medias, ordenados por total; y sus objetivos presupuestarios mensuales:

`hledger balance `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gastos</span>` --monthly --row-total --average --sort-amount --budget`

- Similar a la anterior, de forma más corta, comparando las cuentas por tipo de `Gastos`, como un árbol de dos niveles sin aplastar las cuentas aburridas:

`hledger bal type:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">X</span>` -MTAS --budget -t -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` --no-elide`

- Muestra saldos finales (incluidos los de contabilizaciones anteriores a la fecha de inicio), trimestrales en 2024, en cuentas denominadas `*activos*` o `*pasivos*`:

`hledger balance --historical --period '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">trimestral en 2024</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">activos</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pasivos</span>

- Similar al anterior, de un modo más breve; también muestra saldos en cero, ordena por total y resume a tres niveles:

`hledger bal -HQ date:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2024</span>` type:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AL</span>` -ES -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- Muestra el valor de mercado de los activos de inversión en moneda base al final de cada trimestre:

`hledger bal -HVQ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">activos:inversiones</span>

- Muestra las ganancias/pérdidas de capital no realizadas por cambios en el precio de mercado en cada trimestre, para activos de inversión que no sean criptomonedas:

`hledger bal --gain -Q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">activos:inversiones</span>` not:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">criptomoneda</span>
