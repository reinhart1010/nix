---
layout: page
title: common/antibody (español)
description: "\"El más rápido\" administrador de complementos de shell."
content_hash: 3d261d88dbff24c785941188495d9ca63d595731
last_modified_at: 2023-01-24
related_topics:
  - title: English version
    url: /en/common/antibody.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/antibody.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># antibody

"El más rápido" administrador de complementos de shell.
Más información: <https://getantibody.github.io>.

- Empaqueta todos los complementos para su carga estática:

`antibody bundle < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.zsh_plugins.txt</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.zsh_plugins.sh</span>

- Actualiza todos los empaquetados:

`antibody update`

- Lista todos los complementos instalados:

`antibody list`
