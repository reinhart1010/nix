---
layout: page
title: linux/eselect-repository (español)
description: "Un módulo `eselect` para configurar repositorios ebuild para Portage."
content_hash: ad3c5d5947f4c2488c0ed7bd0a8ed19814f2e523
last_modified_at: 2024-07-30
related_topics:
  - title: English version
    url: /en/linux/eselect-repository.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/eselect-repository.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/eselect-repository.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># eselect repository

Un módulo `eselect` para configurar repositorios ebuild para Portage.
Después de habilitar un repositorio, tienes que ejecutar `emerge --sync repo_name` para descargar ebuilds.
Más información: <https://wiki.gentoo.org/wiki/Eselect/Repository>.

- Lista todos los repositorios ebuild registrados en <https://repos.gentoo.org>:

`eselect repository list`

- Lista de repositorios habilitados:

`eselect repository list -i`

- Habilita un repositorio de la lista según su nombre o índice desde el comando `list`:

`eselect repository enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|index</span>

- Activa un repositorio no registrado:

`eselect repository add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rsync|git|mercurial|svn|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sync_uri</span>

- Deshabilita repositorios sin eliminar su contenido:

`eselect repository disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repo1 repo2 ...</span>

- Desactiva repositorios y elimina su contenido:

`eselect repository remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repo1 repo2 ...</span>

- Crea un repositorio local y lo habilita:

`eselect repository create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/repo</span>
