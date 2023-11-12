---
layout: page
title: common/zip (français)
description: "Empaquette et compresse (archive) les fichiers en un fichier zip."
content_hash: aaa3546837580267ed9d159242ee88911486ca61
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/zip.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/zip.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/zip.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/zip.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># zip

Empaquette et compresse (archive) les fichiers en un fichier zip.
Plus d'informations : <https://manned.org/zip>.

- Empaquette et compresse [r]écursivement un répertoire et son contenu :

`zip -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/du/répertoire</span>

- E[x]clure des fichiers de l'archive :

`zip -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/le/répertoire</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/des/fichiers/exclus</span>

- Archive un répertoire et son contenu avec le plus haut niveau [9] de compression :

`zip -r -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/du/répertoire</span>

- Empaquette et compresse plusieurs répertoires et fichiers :

`zip -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/du/répertoire1 chemin/du/répertoire2 chemin/du/fichier</span>

- Crée une archive chiffrée (l'utilisateur sera sollicité pour saisir le mot de passe) :

`zip -e -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/du/répertoire</span>

- Ajoute des fichiers à une archive existante :

`zip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/du/fichier</span>

- Supprime des fichiers d'une archive existante :

`zip -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive.zip</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo/*.tmp</span>`"`

- Archive un répertoire et son contenu en plusieurs fichiers zip [s]cindés (ex : des fichiers de 3 Go) :

`zip -r -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3g</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/du/répertoire</span>
