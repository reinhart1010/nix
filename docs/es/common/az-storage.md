---
layout: page
title: common/az-storage (español)
description: "Administra los recursos de Azure Cloud Storage."
content_hash: 5d2d33ac963b21d70be2012fbde8b385fd173da7
last_modified_at: 2023-10-14
related_topics:
  - title: English version
    url: /en/common/az-storage.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># az storage

Administra los recursos de Azure Cloud Storage.
Parte de `azure-cli`.
Más información: <https://learn.microsoft.com/cli/azure/storage>.

- Crea una cuenta de almacenamiento:

`az storage account create --resource-group  `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo_de_recursos</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_cuenta</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ubicación</span>` --sku `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">account_sku</span>

- Enumera todas las cuentas de almacenamiento de un grupo de recursos:

`az storage account list --resource-group  `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo_de_recursos</span>

- Enumera las claves de acceso de una cuenta de almacenamiento:

`az storage account keys list --resource-group  `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo_de_recursos</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_cuenta</span>

- Elimina una cuenta de almacenamiento:

`az storage account delete --resource-group  `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo_de_recursos</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_cuenta</span>

- Actualiza la versión mínima de TLS para una cuenta de almacenamiento:

`az storage account update --min-tls-version {TLS1_0|TLS1_1|TLS1_2} --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_cuenta</span>` --resource-group  `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo_de_recursos</span>
