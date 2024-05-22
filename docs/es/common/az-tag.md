---
layout: page
title: common/az-tag (español)
description: "Administra etiquetas en un recurso de Azure."
content_hash: 7ed1ad025e956da3b14402b060cf0552f119b3b8
last_modified_at: 2024-05-22
related_topics:
  - title: English version
    url: /en/common/az-tag.html
    icon: bi bi-globe
tldri18n_status: 2
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

`az tag list --resource-id /subscriptions/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_de_subscripción</span>

- Elimina un valor de etiqueta para un nombre de etiqueta específico:

`az tag remove-value --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_etiqueta</span>` --value `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor_de_etiqueta</span>
