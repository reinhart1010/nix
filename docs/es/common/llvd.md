---
layout: page
title: common/llvd (español)
description: "Descarga videos del sistema de aprendizaje de Linkedin."
content_hash: e6e7b69f7348795d7ed2f71a25228f5f76d87ff1
last_modified_at: 2024-12-29
related_topics:
  - title: English version
    url: /en/common/llvd.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/llvd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# llvd

Descarga videos del sistema de aprendizaje de Linkedin.
Más información: <https://github.com/knowbee/llvd>.

- Descarga un [c]urso utilizando la autenticación basada en cookies:

`llvd -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre-de-curso</span>` --cookies`

- Descarga un curso en una [r]esolución específica:

`llvd -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre-de-curso</span>` -r 720`

- Descarga un curso con subtítulos:

`llvd -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre-de-curso</span>` --caption`

- Descarga un [p]lan de curso con espera entre 10 y 30 segundos:

`llvd -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre-de-plan</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10,30</span>` --cookies`
