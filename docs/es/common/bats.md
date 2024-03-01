---
layout: page
title: common/bats (español)
description: "Bash Automated Testing System: un marco de pruebas compatible con TAP (<https://testanything.org/>) para Bash."
content_hash: 4dbf5716476e9699d1b739556c9999f96dbb1639
last_modified_at: 2024-03-01
related_topics:
  - title: English version
    url: /en/common/bats.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bats

Bash Automated Testing System: un marco de pruebas compatible con TAP (<https://testanything.org/>) para Bash.
Más información: <https://bats-core.readthedocs.io/en/stable/usage.html>.

- Ejecuta un guión de prueba BATS y emite los resultados en el formato TAP (Test Anything Protocol):

`bats --tap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/prueba.bats</span>

- Cuenta los casos de prueba de un guión de prueba sin ejecutar ninguna prueba:

`bats --count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/prueba.bats</span>

- Ejecuta casos de prueba BATS en un directorio y sus subdirectorios (archivos con extensión `.bats`):

`bats --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Obtén resultados en un formato específico:

`bats --formatter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pretty|tap|junit</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/prueba.bats</span>
