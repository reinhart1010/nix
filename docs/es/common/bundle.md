---
layout: page
title: common/bundle (español)
description: "Administrador de dependencias para el lenguaje de programación Ruby."
content_hash: c92f2bf91ac610d0ce4e3d711b057703a37f6f27
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/bundle.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/bundle.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bundle.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bundle.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/bundle.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/bundle.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bundle

Administrador de dependencias para el lenguaje de programación Ruby.
Más información: <https://bundler.io/man/bundle.1.html>.

- Instala todas las gemas (gems) definidas en el archivo `Gemfile` en el directorio de trabajo:

`bundle install`

- Ejecuta un comando en el contexto del paquete (bundle) actual:

`bundle exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumentos</span>

- Actualiza todas las gemas (gems) definidas por las reglas en el `Gemfile` y regenera `Gemfile.lock`:

`bundle update`

- Actualiza una o más gemas específicas definidas en el `Gemfile`:

`bundle update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gema1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gema2</span>

- Actualiza una o más gemas (gems) específicas definidas en el `Gemfile` pero solo a la siguiente versión parche (patch):

`bundle update --patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gema1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gema2</span>

- Actualiza todas las gemas (gems) dentro de un grupo dado en el `Gemfile`:

`bundle update --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">development</span>

- Lista las gemas instaladas con nuevas versiones disponibles definidas en el `Gemfile`:

`bundle outdated`

- Crea una nueva estructura de gema:

`bundle gem `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gema</span>
