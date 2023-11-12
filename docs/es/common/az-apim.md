---
layout: page
title: common/az-apim (español)
description: "Administra los servicios de Azure API Management."
content_hash: 306ead9f55e66b47fb837f07b8e148fec58f32e8
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/az-apim.html
    icon: bi bi-globe
tldri18n_status: 2
---
# az apim

Administra los servicios de Azure API Management.
Parte de `azure-cli` (también conocido como `az`).
Más información: <https://learn.microsoft.com/cli/azure/apim>.

- Enumera las instancias del servicio API Management:

`az apim list --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo_de_recursos</span>

- Crea una instancia de servicio de API Management:

`az apim create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo_de_recursos</span>` --publisher-email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email</span>` --publisher-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Elimina una instancia del servicio de API Management:

`az apim delete --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo_de_recursos</span>

- Muestra detalles de una instancia del servicio de API Management:

`az apim show --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo_de_recursos</span>

- Actualiza una instancia del servicio API Management:

`az apim update --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo_de_recursos</span>
