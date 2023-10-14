---
layout: page
title: common/az-group (español)
description: "Administra grupos de recursos e implementaciones de plantillas."
content_hash: 10674f972ae4917aeb64b4d945ba3ea80fabe006
last_modified_at: 2023-10-14
related_topics:
  - title: English version
    url: /en/common/az-group.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># az group

Administra grupos de recursos e implementaciones de plantillas.
Parte de `azure-cli`.
Más información: <https://docs.microsoft.com/cli/azure/group>.

- Crea un nuevo grupo de recursos:

`az group create --nombre `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` --ubicación `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ubicación</span>

- Comprueba si existe un grupo de recursos:

`az group exists --nombre `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>

- Elimina un grupo de recursos:

`az group delete --nombre `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>

- Coloca un grupo de recursos en estado de espera hasta que se cumpla una condición:

`az group wait --nombre `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">created|deleted|exists|updated</span>
