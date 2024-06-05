---
layout: page
title: common/devenv (español)
description: "Entornos de desarrollo rápidos, declarativos, reproducibles y componibles utilizando Nix."
content_hash: a4f32177c3f3c9e8f652c1e873c895e6b3a1ccb6
last_modified_at: 2024-06-05
related_topics:
  - title: English version
    url: /en/common/devenv.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/devenv.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># devenv

Entornos de desarrollo rápidos, declarativos, reproducibles y componibles utilizando Nix.
Más información: <https://devenv.sh>.

- Inicializa el entorno:

`devenv init`

- Entra en el entorno de desarrollo con hermeticidad relajada (estado de ser hermético):

`devenv shell --impure`

- Obtén información detallada sobre el entorno actual:

`devenv info --verbose`

- Inicia procesos con `devenv`:

`devenv up --config /`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta</span>`/`

- Limpia las variables de entorno y vuelve a entrar en el intérprete de comandos en el modo sin conexión:

`devenv --clean --offline`

- Borra las generaciones anteriores del intérprete de comandos:

`devenv gc`
