---
layout: page
title: common/bats (español)
description: "Bash Automated Testing System: un marco de pruebas compatible con TAP (<https://testanything.org/>) para Bash."
content_hash: 866d646301f949935660eefe2e012f0dce1c1c93
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/bats.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bats.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bats

Bash Automated Testing System: un marco de pruebas compatible con TAP (<https://testanything.org/>) para Bash.
Más información: <https://bats-core.readthedocs.io/en/stable/usage.html>.

- Ejecuta un script de prueba BATS y muestra los resultados en el formato [t]AP (Test Anything Protocol):

`bats --tap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/prueba.bats</span>

- [c]ontar casos de prueba de un script de prueba sin ejecutar ninguna prueba:

`bats --count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/prueba.bats</span>

- Ejecuta casos de prueba BATS [r]ecursivamente (archivos con extensión `.bats`):

`bats --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/directorio</span>

- Muestra los resultados en un [f]ormato específico:

`bats --formatter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pretty|tap|tap13|junit</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/prueba.bats</span>

- Añade información de [T]iming a las pruebas:

`bats --timing `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/prueba.bats</span>

- Ejecuta un número específico de traba[j]os en paralelo (requiere tener instalado GNU `parallel`):

`bats --jobs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/prueba.bats</span>
