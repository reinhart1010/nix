---
layout: page
title: common/az-group (español)
description: "Administra grupos de recursos e implementaciones de plantillas."
content_hash: bdbe78541e35f83c6c446346608a9d395af5ce8d
last_modified_at: 2024-01-02
related_topics:
  - title: English version
    url: /en/common/az-group.html
    icon: bi bi-globe
tldri18n_status: 2
---
# az group

Administra grupos de recursos e implementaciones de plantillas.
Parte de `azure-cli` (también conocido como `az`).
Más información: <https://learn.microsoft.com/cli/azure/group>.

- Crea un nuevo grupo de recursos:

`az group create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` --location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ubicación</span>

- Comprueba si existe un grupo de recursos:

`az group exists --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>

- Elimina un grupo de recursos:

`az group delete --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>

- Coloca un grupo de recursos en estado de espera hasta que se cumpla una condición:

`az group wait --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">created|deleted|exists|updated</span>
