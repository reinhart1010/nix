---
layout: page
title: common/az-account (español)
description: "Administra la información de una suscripción de Azure."
content_hash: b08f57501a1e513424d142f448df717db7ae2d8c
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/az-account.html
    icon: bi bi-globe
tldri18n_status: 2
---
# az account

Administra la información de una suscripción de Azure.
Parte de `azure-cli` (también conocido como `az`).
Más información: <https://learn.microsoft.com/cli/azure/account>.

- Lista las suscripciones de la cuenta activa:

`az account list`

- Establece una `subscription` como la suscripción activa:

`az account set --subscription `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_de_suscripción</span>

- Lista las regiones admitidas para la suscripción activa:

`az account list-locations`

- Imprime un token de acceso para usar con la `MS Graph API`:

`az account get-access-token --resource-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ms-graph</span>

- Imprime los detalles de la suscripción activa actual en un formato específico:

`az account show --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json|tsv|table|yaml</span>
