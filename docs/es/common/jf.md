---
layout: page
title: common/jf (español)
description: "Interactúa con productos JFrog como Artifactory, Xray, Distribution, Pipelines Mission Control."
content_hash: 1877d1f13e295a714091bec30a82e605d1a0e483
last_modified_at: 2024-11-18
related_topics:
  - title: English version
    url: /en/common/jf.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/jf.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/jf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jf

Interactúa con productos JFrog como Artifactory, Xray, Distribution, Pipelines Mission Control.
Más información: <https://jfrog.com/help/r/jfrog-cli/usage>.

- Añade una nueva configuración:

`jf config add`

- Muestra la configuración actual:

`jf config show`

- Busca artefactos dentro del repositorio y directorio dados:

`jf rt search --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_repositorio</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta</span>`/`
