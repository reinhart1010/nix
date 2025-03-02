---
layout: page
title: common/install (français)
description: "Copie des fichiers et met à jour leurs attributs."
content_hash: 507a246b57dcfa02764e612d6aa98b5937bf0aa2
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/install.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/install.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/install.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/install.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># install

Copie des fichiers et met à jour leurs attributs.
Copie des fichiers (souvent des exécutables) dans un répertoire système comme `/usr/local/bin` et leur donne les permissions et propriétaires appropriés.
Plus d'informations : <https://www.gnu.org/software/coreutils/manual/html_node/install-invocation.html>.

- Copie des fichiers vers une destination :

`install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/fichier/source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/repertoire/destination</span>

- Copie des fichiers vers une destination en mettant à jour leur propriétaire :

`install --owner `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">utilisateur</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/fichier/source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/repertoire/destination</span>

- Copie des fichiers vers une destination en mettant à jour leur groupe d'appartenance :

`install --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">utilisateur</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/fichier/source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/repertoire/destination</span>

- Copie des fichiers vers une destination en mettant à jour leur mode :

`install --mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+x</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/fichier/source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/repertoire/destination</span>

- Copie des fichiers en mettant à jour leur dates d'accès et de modification à partir de leurs sources respectives :

`install --preserve-timestamps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/fichier/source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/repertoire/destination</span>
