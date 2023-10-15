---
layout: page
title: common/az-tag (español)
description: "Administra etiquetas en un recurso de Azure."
content_hash: 14d02c7dd6c4e1e82597e5a90e3b1d613c6bbad5
last_modified_at: 2023-10-15
related_topics:
  - title: English version
    url: /en/common/az-tag.html
    icon: bi bi-globe
---
# az tag

Administra etiquetas en un recurso de Azure.
Parte de `azure-cli` (también conocido como `az`).
Más información: <https://learn.microsoft.com/cli/azure/tag>.

- Crea un valor de etiqueta:

`az tag add-value --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_etiqueta</span>` --value `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor_de_etiqueta</span>

- Crea una etiqueta en la suscripción:

`az tag create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_etiqueta</span>

- Elimina una etiqueta de la suscripción:

`az tag delete --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_etiqueta</span>

- Enumera todas las etiquetas de una suscripción:

`az tag list --resource-id /subscriptions/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subscription_id</span>

- Elimina un valor de etiqueta para un nombre de etiqueta específico:

`az tag remove-value --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_etiqueta</span>` --value `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor_de_etiqueta</span>
