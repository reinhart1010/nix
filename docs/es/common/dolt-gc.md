---
layout: page
title: common/dolt-gc (español)
description: "Busca en el repositorio los datos que ya no se referencian ni necesitan."
content_hash: 818356baec30d28531d01fdf774173d6fd49edcb
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/common/dolt-gc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dolt-gc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dolt gc

Busca en el repositorio los datos que ya no se referencian ni necesitan.
Más información: <https://docs.dolthub.com/cli-reference/cli#dolt-gc>.

- Limpia datos no referenciados del repositorio:

`dolt gc`

- Inicia un proceso de recolección de basura más rápido pero menos exhaustivo:

`dolt gc --shallow`
