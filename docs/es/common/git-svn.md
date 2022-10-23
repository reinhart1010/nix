---
layout: page
title: common/git-svn (español)
description: "Operacion bidreccional entre un repositorio Subversión y otro Git."
content_hash: cba60761e8b4b862d8c691909ced919a1cd4500c
related_topics:
  - title: English version
    url: /en/common/git-svn.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-svn.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-svn.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-svn.html
    icon: bi bi-globe
---
# git svn

Operacion bidreccional entre un repositorio Subversión y otro Git.
Más información: <https://git-scm.com/docs/git-svn>.

- Clona un repositorio SVN:

`git svn clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://ejemplo.com/repositorio_subversion</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directorio_local</span>

- Clona un repositorio SVN a partir un número de revisión específico:

`git svn clone -r`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>`:HEAD `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://svn.ejemplo.net/subversion/repo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directorio_local</span>

- Actualiza el clon local a partir del repositorio SVN:

`git svn rebase`

- Obtiene las actualización del repositorio SVN remoto sin cambiar el HEAD de Git:

`git svn fetch`

- Realiza un commit al repositorio SVN:

`git svn dcommit`
