---
layout: page
title: common/git-cola (español)
description: "Una poderosa interfaz gráfica de Usuario (GUI) Git con experiencia de usuario ágil e intuitiva."
content_hash: 4c11db5d286b3356ea7c1880bee2924677da1860
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/common/git-cola.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-cola.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-cola.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/git-cola.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-cola.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git cola

Una poderosa interfaz gráfica de Usuario (GUI) Git con experiencia de usuario ágil e intuitiva.
Más información: <https://git-cola.readthedocs.io>.

- Inicia la GUI:

`git cola`

- Inicia la GUI en modo de enmienda (amend  mode):

`git cola --amend`

- Apunta a un repositorio Git. Predeterminado al directorio actual:

`git cola --prompt`

- Abre el repositorio Git en la ruta mencionada:

`git cola --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/repositorio-git</span>

- Aplica el filtro de ruta al componente gráfico de estado:

`git cola --status-filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filtro</span>
