---
layout: page
title: common/pulumi-state (español)
description: "Edita el estado de la pila actual."
content_hash: a20763aa997cd5af1079ddb84795c8c57e326f11
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/pulumi-state.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pulumi state

Edita el estado de la pila actual.
Más información: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_state/>.

- Elimina un recurso del estado de la pila actual:

`pulumi state delete`

- Mueve un recurso de la pila actual a otra:

`pulumi state move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">recurso_urn</span>` --dest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_pila</span>

- Cambia el nombre de un recurso de la pila actual:

`pulumi state rename`

- Repara un estado no válido:

`pulumi state repair`

- Muestra la ayuda:

`pulumi state --help`
