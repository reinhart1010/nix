---
layout: page
title: common/az-storage (español)
description: "Administra los recursos de Azure Cloud Storage."
content_hash: 55b2d86e904b8378d73df29318cb983f9c3fb51a
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/az-storage.html
    icon: bi bi-globe
tldri18n_status: 2
---
# az storage

Administra los recursos de Azure Cloud Storage.
Parte de `azure-cli` (también conocido como `az`).
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
