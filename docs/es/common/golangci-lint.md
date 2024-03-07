---
layout: page
title: common/golangci-lint (español)
description: "Corredor de linters Go paralelizado, inteligente y rápido que se integra con los principales entornos de desarrollo integrado y soporta configuración en YAML."
content_hash: 66b7473b6e78f1d77dec872e2de9fd2e4d803294
last_modified_at: 2024-03-07
related_topics:
  - title: English version
    url: /en/common/golangci-lint.html
    icon: bi bi-globe
tldri18n_status: 2
---
# golangci-lint

Corredor de linters Go paralelizado, inteligente y rápido que se integra con los principales entornos de desarrollo integrado y soporta configuración en YAML.
Más información: <https://golangci-lint.run/usage/quick-start/>.

- Ejecuta linters en la carpeta actual:

`golangci-lint run`

- Lista los linters habilitados y deshabilitados (Nota: los linters deshabilitados se muestran en el último lugar, no los confundas con los habilitados):

`golangci-lint linters`

- Habilita un linter específico para esta ejecución:

`golangci-lint run --enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linter</span>
