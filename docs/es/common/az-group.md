---
layout: page
title: common/az-group (español)
description: "Administra grupos de recursos e implementaciones de plantillas."
content_hash: fa8ba0b295c1395d6dfa8c7bb46ed1caed53a060
last_modified_at: 2023-11-12
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

`az group create --nombre `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` --ubicación `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ubicación</span>

- Comprueba si existe un grupo de recursos:

`az group exists --nombre `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>

- Elimina un grupo de recursos:

`az group delete --nombre `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>

- Coloca un grupo de recursos en estado de espera hasta que se cumpla una condición:

`az group wait --nombre `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">created|deleted|exists|updated</span>
