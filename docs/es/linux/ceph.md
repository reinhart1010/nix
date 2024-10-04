---
layout: page
title: linux/ceph (español)
description: "Un sistema de almacenamiento unificado."
content_hash: 1caae1ba1dc2726d17852a9aab1767a74c2f8494
last_modified_at: 2024-10-04
related_topics:
  - title: English version
    url: /en/linux/ceph.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ceph

Un sistema de almacenamiento unificado.
Más información: <https://ceph.io/en>.

- Comprueba el estado del cluster:

`ceph status`

- Comprueba las estadísticas de uso del cluster:

`ceph df`

- Obtiene las estadísticas de los grupos de colocación de un cluster:

`ceph pg dump --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plain</span>

- Crea un grupo de almacenamiento:

`ceph osd pool create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_pool</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_de_página</span>

- Elimina un pool de almacenamiento:

`ceph osd pool delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_pool</span>

- Cambia el nombre de un pool de almacenamiento:

`ceph osd pool rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_actual</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_nuevo</span>

- Auto-repara pool de almacenamiento:

`ceph pg repair `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_pool</span>
